from tkinter import Label, Entry, Button, StringVar, messagebox
from ui.navigation import show_main_menu
from ui.menu import build_global_menu  # Преход в меню зліва сторінки
from modules.data_store import set_result, get_result  # Додано get_result


def SocialTaxCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()
    build_global_menu(root)

    root.title("Розрахунок З_н — соціальні відрахування")

    def calculate_social_tax():
        try:
            Z_o = float(entry_Zo.get())
            Z_r = float(entry_Zr.get())
            Z_dod = float(entry_Zdod.get())
            H_soc = float(entry_Hsoc.get())

            Zn = (Z_o + Z_r + Z_dod) * H_soc / 100
            result_var.set(f"Відрахування З_н: {Zn:.2f} грн")
            set_result("З_н", Zn)  # ← Зберігаємо результат
        except ValueError:
            messagebox.showerror("Помилка", "Перевірте правильність введених чисел")

    Label(root, text="Z_o (ЗП дослідників)").grid(row=0, column=0, sticky="e")
    entry_Zo = Entry(root)
    entry_Zo.grid(row=0, column=1)

    Label(root, text="Z_p (ЗП робітників)").grid(row=1, column=0, sticky="e")
    entry_Zr = Entry(root)
    entry_Zr.grid(row=1, column=1)

    Label(root, text="Z_дод (додаткова ЗП)").grid(row=2, column=0, sticky="e")
    entry_Zdod = Entry(root)
    entry_Zdod.grid(row=2, column=1)

    Label(root, text="H_зп (%)").grid(row=3, column=0, sticky="e")
    entry_Hsoc = Entry(root)
    entry_Hsoc.insert(0, "22")
    entry_Hsoc.grid(row=3, column=1)

    # 🟦 Автоматичне підставлення значень збережених ЗП
    zo = get_result("З_o")
    zp = get_result("З_p")
    zdod = get_result("З_дод")
    if zo is not None:
        entry_Zo.insert(0, f"{zo:.2f}")
    if zp is not None:
        entry_Zr.insert(0, f"{zp:.2f}")
    if zdod is not None:
        entry_Zdod.insert(0, f"{zdod:.2f}")

    Button(root, text="Розрахувати", command=calculate_social_tax).grid(row=4, columnspan=2, pady=10)

    result_var = StringVar()
    Label(root, textvariable=result_var, fg="blue").grid(row=5, columnspan=2)

    Button(root, text="Назад", command=lambda: show_main_menu(root)).grid(row=6, columnspan=2, pady=10)
