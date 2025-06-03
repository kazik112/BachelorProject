from tkinter import Tk, Label, Entry, Button, StringVar, Frame, messagebox
from ui.navigation import show_main_menu
from ui.menu import build_global_menu
from modules.data_store import set_result

def MaterialCostCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()

    build_global_menu(root)
    root.title("Розрахунок M — витрати на матеріали")

    # Ввід кількості рядків
    Label(root, text="Кількість видів матеріалів (n):").pack()
    row_count_var = StringVar(value="3")
    Entry(root, textvariable=row_count_var, width=5).pack()

    def calculate_material_cost():
        try:
            rows = []
            for i in range(int(row_count_var.get())):
                hj = float(entries[i]['hj'].get())
                cj = float(entries[i]['cj'].get())
                kj = float(entries[i]['kj'].get())
                bj = float(entries[i]['bj'].get())
                cebj = float(entries[i]['cebj'].get())
                rows.append(hj * cj * kj - bj * cebj)

            M = sum(rows)
            result_var.set(f"Загальні витрати на матеріали M = {M:.2f} грн")
            set_result("M", M)
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення.")

    def generate_fields():
        for widget in input_frame.winfo_children():
            widget.destroy()
        entries.clear()

        try:
            row_count = int(row_count_var.get())
            headers = ["Hj (норма витрат, кг)", "Цj (грн/кг)", "Kj", "Bj (втрати, кг)", "Цвj (грн/кг)"]
            for col, header in enumerate(headers):
                Label(input_frame, text=header, font=("Arial", 9, "bold")).grid(row=0, column=col, padx=5, pady=2)

            for i in range(row_count):
                row_entries = {}
                for j, key in enumerate(['hj', 'cj', 'kj', 'bj', 'cebj']):
                    entry = Entry(input_frame, width=10)
                    entry.grid(row=i + 1, column=j, padx=5, pady=2)
                    row_entries[key] = entry
                entries.append(row_entries)
        except ValueError:
            messagebox.showerror("Помилка", "Введіть кількість рядків як ціле число.")

    Button(root, text="Створити таблицю", command=generate_fields).pack(pady=5)

    input_frame = Frame(root)
    input_frame.pack()

    entries = []

    Button(root, text="Розрахувати", command=calculate_material_cost).pack(pady=10)

    result_var = StringVar()
    Label(root, textvariable=result_var, fg="blue", font=("Arial", 10, "bold")).pack()

    Button(root, text="Назад", command=lambda: show_main_menu(root)).pack(pady=5)
