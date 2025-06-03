from tkinter import Label, Entry, Button, StringVar, messagebox
from ui.navigation import show_main_menu
from ui.menu import build_global_menu
from modules.data_store import set_result

def OtherExpensesCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()

    build_global_menu(root)
    root.title("Розрахунок І_в — інші витрати")

    def calculate_other_expenses():
        try:
            Zo = float(entry_Zo.get())
            Zp = float(entry_Zp.get())
            Hiv = float(entry_Hiv.get())

            Iv = round((Zo + Zp) * Hiv / 100, 2)
            result_var.set(f"Інші витрати І_в = {Iv:.2f} грн")
            set_result("І_в", Iv)
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення.")

    Label(root, text="З_o (ЗП дослідників), грн:").grid(row=0, column=0, sticky='e')
    entry_Zo = Entry(root)
    entry_Zo.grid(row=0, column=1)

    Label(root, text="З_p (ЗП робітників), грн:").grid(row=1, column=0, sticky='e')
    entry_Zp = Entry(root)
    entry_Zp.grid(row=1, column=1)

    Label(root, text="Н_ів (% інших витрат):").grid(row=2, column=0, sticky='e')
    entry_Hiv = Entry(root)
    entry_Hiv.insert(0, "2")
    entry_Hiv.grid(row=2, column=1)

    Button(root, text="Розрахувати", command=calculate_other_expenses).grid(row=3, column=0, columnspan=2, pady=10)

    result_var = StringVar()
    Label(root, textvariable=result_var, fg="blue").grid(row=4, column=0, columnspan=2)

    Button(root, text="Назад", command=lambda: show_main_menu(root)).grid(row=5, column=0, columnspan=2, pady=10)
