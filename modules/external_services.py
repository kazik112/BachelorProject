from tkinter import Label, Entry, Button, StringVar, messagebox
from ui.navigation import show_main_menu
from ui.menu import build_global_menu
from modules.data_store import set_result

def ExternalServicesCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()

    build_global_menu(root)
    root.title("Розрахунок B_сп — витрати на сторонні роботи")

    def calculate_external_services():
        try:
            Zo = float(entry_Zo.get())
            Zp = float(entry_Zp.get())
            Hsn = float(entry_Hsn.get())

            Bsn = round((Zo + Zp) * Hsn / 100, 2)
            result_var.set(f"Витрати на сторонні роботи B_сп = {Bsn:.2f} грн")
            set_result("B_сп", Bsn)
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення.")

    Label(root, text="З_o (основна ЗП дослідників), грн:").grid(row=0, column=0, sticky='e')
    entry_Zo = Entry(root)
    entry_Zo.grid(row=0, column=1)

    Label(root, text="З_p (основна ЗП робітників), грн:").grid(row=1, column=0, sticky='e')
    entry_Zp = Entry(root)
    entry_Zp.grid(row=1, column=1)

    Label(root, text="Н_сп (% витрат на сторонні роботи):").grid(row=2, column=0, sticky='e')
    entry_Hsn = Entry(root)
    entry_Hsn.insert(0, "5")  # значення за замовчуванням
    entry_Hsn.grid(row=2, column=1)

    Button(root, text="Розрахувати", command=calculate_external_services).grid(row=3, column=0, columnspan=2, pady=10)

    result_var = StringVar()
    Label(root, textvariable=result_var, fg="blue").grid(row=4, column=0, columnspan=2)

    Button(root, text="Назад", command=lambda: show_main_menu(root)).grid(row=5, column=0, columnspan=2, pady=10)
