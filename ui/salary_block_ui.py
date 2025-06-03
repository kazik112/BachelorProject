import tkinter as tk
from modules.salary_zo import SalaryZoCalculator, set_zdod_block as set_zdod_block_zo
from modules.salary_zp import SalaryZpCalculator, set_zdod_block as set_zdod_block_zp
from modules.salary_zdod import SalaryZdodCalculator

from ui.navigation import show_main_menu
from ui.menu import build_global_menu


def open_salary_block(root):
    for widget in root.winfo_children():
        widget.destroy()

    build_global_menu(root)

    tk.Label(root, text="Витрати на оплату праці", font=("Arial", 16, "bold")).pack(pady=10)

    SalaryZoCalculator(root)
    SalaryZpCalculator(root)

    zdod_block = SalaryZdodCalculator(root)

    set_zdod_block_zo(zdod_block)  # 🔁 передаємо в Zo
    set_zdod_block_zp(zdod_block)  # ✅ передаємо в Zp

    tk.Button(root, text="Назад", command=lambda: show_main_menu(root)).pack(pady=10)
