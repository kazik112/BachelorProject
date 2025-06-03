# ui/main_window.py

import tkinter as tk
from ui.navigation import show_main_menu

def MainWindow(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Програмний модуль розрахунку витрат на НДР")
    root.geometry("500x300")
    root.configure(bg="#f5f5f5")

    # Заголовок
    tk.Label(
        root,
        text="Головне меню",
        font=("Arial", 20, "bold"),
        bg="#f5f5f5",
        fg="#2c3e50"
    ).pack(pady=(30, 10))

    # Пояснення
    tk.Label(
        root,
        text="Програма для розрахунку витрат на науково-дослідну роботу",
        font=("Arial", 12),
        bg="#f5f5f5",
        fg="#333"
    ).pack(pady=(0, 20))

    # Кнопка переходу
    tk.Button(
        root,
        text="Перейти до розрахунків",
        font=("Arial", 12, "bold"),
        bg="#2980b9",
        fg="white",
        relief="raised",
        bd=3,
        padx=15,
        pady=5,
        command=lambda: show_main_menu(root)
    ).pack()
