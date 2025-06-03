from tkinter import Label, Entry, Button, StringVar, messagebox
from ui.navigation import show_main_menu
from ui.menu import build_global_menu  # Додаємо глобальне меню
from modules.data_store import set_result  # Для збереження результату
import tkinter as tk

def ComponentsCostCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()

    build_global_menu(root)  # Додати меню

    root.title("Розрахунок Ke — витрати на комплектуючі")

    entries = []

    def calculate_components_cost():
        try:
            rows = []
            for i in range(int(row_count_var.get())):
                hj = float(entries[i]['hj'].get())
                cj = float(entries[i]['cj'].get())
                kj = float(entries[i]['kj'].get())
                rows.append(hj * cj * kj)
            Ke = sum(rows)
            result_var.set(f"Загальні витрати на комплектуючі Ke = {Ke:.2f} грн")
            set_result("K_е", Ke)  # Зберігаємо для TotalCostCalculator
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення.")

    def generate_fields():
        for widget in input_frame.winfo_children():
            widget.destroy()
        entries.clear()
        try:
            row_count = int(row_count_var.get())
            headers = ["Hj (кількість, шт)", "Цj (грн/шт)", "Kj (коеф. транспортування)"]
            for col, header in enumerate(headers):
                Label(input_frame, text=header, font=("Arial", 9, "bold")).grid(row=0, column=col, padx=5, pady=2)
            for i in range(row_count):
                row_entries = {}
                for j, key in enumerate(['hj', 'cj', 'kj']):
                    entry = Entry(input_frame, width=10)
                    entry.grid(row=i + 1, column=j, padx=5, pady=2)
                    row_entries[key] = entry
                entries.append(row_entries)
        except ValueError:
            messagebox.showerror("Помилка", "Введіть кількість рядків як ціле число.")

    Label(root, text="Кількість найменувань комплектуючих (n):").pack()
    row_count_var = StringVar(value="3")
    Entry(root, textvariable=row_count_var, width=5).pack()
    Button(root, text="Створити таблицю", command=generate_fields).pack(pady=5)

    input_frame = tk.Frame(root)
    input_frame.pack()

    Button(root, text="Розрахувати", command=calculate_components_cost).pack(pady=10)

    result_var = StringVar()
    Label(root, textvariable=result_var, fg="blue", font=("Arial", 10, "bold")).pack()

    Button(root, text="Назад", command=lambda: show_main_menu(root)).pack(pady=10)

    generate_fields()
