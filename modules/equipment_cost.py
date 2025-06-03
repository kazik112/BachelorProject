from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame
from ui.navigation import show_main_menu
from ui.menu import build_global_menu  # ← Глобальне меню
from modules.data_store import set_result  # ← Збереження результатів

def EquipmentCostCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()

    build_global_menu(root)  # Додаємо меню

    root.title("Розрахунок B_спец — Спецустаткування для наукових робіт")

    rows = []

    def calculate_equipment_cost():
        try:
            total = 0
            for row in rows:
                price = float(row["price"].get())
                count = int(row["count"].get())
                coef = float(row["coef"].get())
                total += price * count * coef
            result_var.set(f"Балансова вартість устаткування: {total:.2f} грн")
            set_result("B_спец", total)  # ← Зберігаємо результат
        except ValueError:
            messagebox.showerror("Помилка", "Перевірте правильність введених чисел")

    def update_rows():
        for widget in frame_rows.winfo_children():
            widget.destroy()
        rows.clear()
        try:
            count = int(entry_count.get())
        except ValueError:
            messagebox.showerror("Помилка", "Введіть кількість найменувань як число")
            return

        Label(frame_rows, text="№").grid(row=0, column=0)
        Label(frame_rows, text="Ціна за одиницю (Ці), грн").grid(row=0, column=1)
        Label(frame_rows, text="Кількість одиниць (Cnp.i), шт").grid(row=0, column=2)
        Label(frame_rows, text="Коефіцієнт (Ki)").grid(row=0, column=3)

        for i in range(count):
            Label(frame_rows, text=f"{i+1}").grid(row=i+1, column=0)
            e_price = Entry(frame_rows, width=15)
            e_price.grid(row=i+1, column=1)
            e_count = Entry(frame_rows, width=15)
            e_count.grid(row=i+1, column=2)
            e_coef = Entry(frame_rows, width=15)
            e_coef.grid(row=i+1, column=3)
            rows.append({"price": e_price, "count": e_count, "coef": e_coef})

    Label(root, text="Кількість найменувань:").grid(row=0, column=0)
    entry_count = Entry(root)
    entry_count.grid(row=0, column=1)
    Button(root, text="Створити таблицю", command=update_rows).grid(row=0, column=2)

    frame_rows = Frame(root)
    frame_rows.grid(row=1, column=0, columnspan=3, pady=10)

    Button(root, text="Розрахувати", command=calculate_equipment_cost).grid(row=2, column=0, columnspan=3)

    result_var = StringVar()
    Label(root, textvariable=result_var, fg="blue").grid(row=3, column=0, columnspan=3)

    Button(root, text="Назад", command=lambda: show_main_menu(root)).grid(row=4, column=0, columnspan=3, pady=10)
