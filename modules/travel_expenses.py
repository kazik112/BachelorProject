from tkinter import Label, Entry, Button, StringVar, messagebox
from ui.navigation import show_main_menu
from ui.menu import build_global_menu  # меню зліва
from modules.data_store import set_result  # збереження значення

def TravelExpensesCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()

    build_global_menu(root)
    root.title("Розрахунок B_св — службові відрядження")

    def calculate_travel_expenses():
        try:
            Zo = float(entry_Zo.get())
            Zp = float(entry_Zp.get())
            Hsv = float(entry_Hsv.get())

            Bsv = round((Zo + Zp) * Hsv / 100, 2)
            result_var.set(f"Витрати на службові відрядження B_св = {Bsv:.2f} грн")
            set_result("B_св", Bsv)
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення.")

    Label(root, text="З_o (основна зарплата), грн:").grid(row=0, column=0, sticky='e')
    entry_Zo = Entry(root)
    entry_Zo.grid(row=0, column=1)

    Label(root, text="З_p (зарплата робітників), грн:").grid(row=1, column=0, sticky='e')
    entry_Zp = Entry(root)
    entry_Zp.grid(row=1, column=1)

    Label(root, text="Н_св (% нарахувань):").grid(row=2, column=0, sticky='e')
    entry_Hsv = Entry(root)
    entry_Hsv.insert(0, "5")  # значення за замовчуванням
    entry_Hsv.grid(row=2, column=1)

    Button(root, text="Розрахувати", command=calculate_travel_expenses).grid(row=3, column=0, columnspan=2, pady=10)

    result_var = StringVar()
    Label(root, textvariable=result_var, fg="blue").grid(row=4, column=0, columnspan=2)

    Button(root, text="Назад", command=lambda: show_main_menu(root)).grid(row=5, column=0, columnspan=2, pady=5)
