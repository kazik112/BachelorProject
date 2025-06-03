from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from ui.navigation import show_main_menu
from ui.menu import build_global_menu  # ← глобальне меню
from modules.data_store import set_result  # ← збереження

def AmortizationCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()

    build_global_menu(root)  # ← Додати меню
    root.title("Розрахунок A_обл — амортизація")

    def calculate_amortization():
        try:
            Cz = float(entry_Cz.get())      # Цб – балансова вартість
            Tg = float(entry_Tg.get())      # Тв – строк використання, років
            t_vyk = float(entry_t_vyk.get())  # tвик – тривалість використання, міс.

            A_obl = round((Cz / Tg) * (t_vyk / 12), 2)
            result_var.set(f"А_обл = {A_obl:.2f} грн")
            set_result("A_обл", A_obl)  # ← збереження в пам’ять
        except ValueError:
            messagebox.showerror("Помилка", "Перевірте правильність введених чисел")

    Label(root, text="Цб (балансова вартість), грн").grid(row=0, column=0, sticky="w")
    entry_Cz = Entry(root)
    entry_Cz.grid(row=0, column=1)

    Label(root, text="Тв (строк використання), років").grid(row=1, column=0, sticky="w")
    entry_Tg = Entry(root)
    entry_Tg.grid(row=1, column=1)

    Label(root, text="tвик (термін використання), міс.").grid(row=2, column=0, sticky="w")
    entry_t_vyk = Entry(root)
    entry_t_vyk.grid(row=2, column=1)

    Button(root, text="Розрахувати", command=calculate_amortization).grid(row=3, column=0, columnspan=2, pady=10)

    result_var = StringVar()
    Label(root, textvariable=result_var, fg="blue").grid(row=4, column=0, columnspan=2)

    Button(root, text="Назад", command=lambda: show_main_menu(root)).grid(row=5, column=0, columnspan=2, pady=10)
