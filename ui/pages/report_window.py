import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from modules.data_store import get_result
from ui.navigation import show_main_menu

import csv
import pandas as pd

REPORT_ITEMS = [
    ("З_o", "Зарплата дослідників"),
    ("З_p", "Зарплата робітників"),
    ("З_дод", "Додаткова зарплата"),
    ("З_н", "Соціальні відрахування"),
    ("M", "Матеріали"),
    ("K_е", "Комплектуючі"),
    ("B_спец", "Спецустаткування"),
    ("B_пз", "Програмне забезпечення"),
    ("A_обл", "Амортизація обладнання"),
    ("B_е", "Енерговитрати"),
    ("B_св", "Службові відрядження"),
    ("B_сп", "Сторонні роботи"),
    ("І_в", "Інші витрати"),
    ("B_нзв", "Накладні витрати"),
]

def open_report_window(root):
    for widget in root.winfo_children():
        widget.destroy()

    from ui.menu import build_global_menu
    build_global_menu(root)

    root.title("Звіт про витрати")
    tk.Label(root, text="Проміжні результати розрахунків", font=("Arial", 14, "bold")).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack()

    tree = ttk.Treeview(frame, columns=("name", "value"), show="headings")
    tree.heading("name", text="Назва")
    tree.heading("value", text="Значення (грн)")
    tree.column("name", width=250)
    tree.column("value", width=150)
    tree.pack()

    results = []
    total = 0.0
    for key, label in REPORT_ITEMS:
        value = get_result(key)
        if value is not None:
            results.append((label, round(value, 2)))
            tree.insert("", "end", values=(label, f"{value:.2f}"))
            total += value
        else:
            results.append((label, 0.00))
            tree.insert("", "end", values=(label, "-"))

    total_label = tk.Label(root, text=f"Підсумкова сума B_заг = {total:.2f} грн", font=("Arial", 12, "bold"), fg="blue")
    total_label.pack(pady=10)

    def save_report():
        filetypes = [
            ("CSV файли", "*.csv"),
            ("Excel файли", "*.xlsx"),
        ]
        path = filedialog.asksaveasfilename(
            title="Зберегти звіт",
            defaultextension=".csv",
            filetypes=filetypes
        )
        if not path:
            return

        try:
            if path.endswith(".csv"):
                with open(path, "w", newline='', encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Назва", "Значення (грн)"])
                    for name, value in results:
                        writer.writerow([name, value])
                    writer.writerow(["Підсумок", round(total, 2)])
            elif path.endswith(".xlsx"):
                df = pd.DataFrame(results, columns=["Назва", "Значення (грн)"])
                df.loc[len(df)] = ["Підсумок", round(total, 2)]
                df.to_excel(path, index=False)
            messagebox.showinfo("Успіх", "Звіт успішно збережено!")
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося зберегти: {e}")

    buttons = tk.Frame(root)
    buttons.pack(pady=10)

    tk.Button(buttons, text="Зберегти як...", command=save_report).pack(side="left", padx=5)
    tk.Button(buttons, text="Назад", command=lambda: show_main_menu(root)).pack(side="left", padx=5)
