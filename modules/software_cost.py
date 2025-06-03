import tkinter as tk
from tkinter import messagebox
from ui.navigation import show_main_menu
from ui.menu import build_global_menu  # ← Глобальне меню
from modules.data_store import set_result  # ← Збереження результату

def SoftwareCostCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()

    build_global_menu(root)  # ← Додаємо глобальне меню

    root.title("Розрахунок B_пз — Програмне забезпечення")

    def calculate_B_pz():
        try:
            k = int(entry_k.get())
            total = 0.0
            for i in range(k):
                price = float(entry_grid[i][0].get())      # Ціна
                count = float(entry_grid[i][1].get())      # Кількість
                coef = float(entry_grid[i][2].get())       # Коефіцієнт
                total += price * count * coef
            result_var.set(f"Балансова вартість ПЗ: {total:.2f} грн")
            set_result("B_пз", total)  # ← Зберігаємо результат
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення.")

    def generate_inputs():
        for widget in frame_inputs.winfo_children():
            widget.destroy()
        try:
            k = int(entry_k.get())
        except ValueError:
            messagebox.showerror("Помилка", "Введіть кількість найменувань цілим числом.")
            return

        nonlocal entry_grid
        entry_grid = []

        tk.Label(frame_inputs, text="Ціна").grid(row=0, column=1)
        tk.Label(frame_inputs, text="Кількість").grid(row=0, column=2)
        tk.Label(frame_inputs, text="Коефіцієнт").grid(row=0, column=3)

        for i in range(k):
            tk.Label(frame_inputs, text=f"ПЗ {i + 1}").grid(row=i + 1, column=0, sticky="w")
            row_entries = []
            for j in range(3):
                e = tk.Entry(frame_inputs, width=10)
                e.grid(row=i + 1, column=j + 1)
                row_entries.append(e)
            entry_grid.append(row_entries)

        tk.Button(frame_inputs, text="Розрахувати", command=calculate_B_pz).grid(row=k + 1, columnspan=4, pady=10)
        tk.Label(frame_inputs, textvariable=result_var, fg="blue").grid(row=k + 2, columnspan=4)

    tk.Label(root, text="Кількість найменувань:").pack()
    entry_k = tk.Entry(root)
    entry_k.pack()
    tk.Button(root, text="Створити таблицю", command=generate_inputs).pack()

    frame_inputs = tk.Frame(root)
    frame_inputs.pack()

    entry_grid = []
    result_var = tk.StringVar()

    tk.Button(root, text="Назад", command=lambda: show_main_menu(root)).pack(pady=5)

    
