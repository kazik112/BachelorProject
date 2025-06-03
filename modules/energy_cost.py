import tkinter as tk
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from ui.navigation import show_main_menu
from ui.menu import build_global_menu  # Додаємо глобальне меню
from modules.data_store import set_result  # Збереження результатів

def EnergyCostCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()

    build_global_menu(root)
    root.title("Розрахунок Bе — витрати на енергію")

    input_rows = []

    def calculate_energy_cost():
        try:
            total = 0
            for row in input_rows:
                W = float(row[0].get())
                t = float(row[1].get())
                Ce = float(row[2].get())
                K = float(row[3].get())
                eta = float(row[4].get())
                cost = round((W * t * Ce * K) / eta, 2)
                row[5].config(text=f"{cost:.2f}")
                total += cost
            total = round(total, 2)
            result_var.set(f"Загальні витрати Bе = {total:.2f} грн")
            set_result("B_е", total)
        except ValueError:
            messagebox.showerror("Помилка", "Перевірте правильність введених чисел")

    def create_table():
        try:
            count = int(entry_count.get())
            for widget in frame_table.winfo_children():
                widget.destroy()
            input_rows.clear()
            headers = ["W (кВт)", "t (год)", "Це (грн)", "K", "η", "Вартість (грн)"]
            for col, text in enumerate(headers):
                Label(frame_table, text=text, font=('Arial', 10, 'bold')).grid(row=0, column=col, padx=5, pady=2)

            for i in range(count):
                row = []
                for j in range(5):
                    e = Entry(frame_table, width=10)
                    e.grid(row=i+1, column=j, padx=5, pady=2)
                    row.append(e)
                lbl = Label(frame_table, text="0.00")
                lbl.grid(row=i+1, column=5, padx=5, pady=2)
                row.append(lbl)
                input_rows.append(row)

        except ValueError:
            messagebox.showerror("Помилка", "Введіть ціле число кількості пристроїв")

    Label(root, text="Кількість пристроїв:").grid(row=0, column=0)
    entry_count = Entry(root, width=5)
    entry_count.insert(0, "1")  # ← Щоб уникнути помилки при старті
    entry_count.grid(row=0, column=1)

    Button(root, text="Створити таблицю", command=create_table).grid(row=0, column=2, padx=10)

    frame_table = tk.Frame(root)
    frame_table.grid(row=1, column=0, columnspan=6)

    Button(root, text="Розрахувати", command=calculate_energy_cost).grid(row=2, column=0, columnspan=3, pady=10)
    result_var = StringVar()
    Label(root, textvariable=result_var, fg="blue").grid(row=3, column=0, columnspan=6)

    Button(root, text="Назад", command=lambda: show_main_menu(root)).grid(row=4, column=0, columnspan=6, pady=10)
