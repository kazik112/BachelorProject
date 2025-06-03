from tkinter import Label, Entry, Button, StringVar, messagebox
from ui.navigation import show_main_menu
from modules.data_store import get_result

def TotalCostCalculator(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Підсумковий розрахунок B_заг")

    labels = [
        "З_o", "З_p", "З_дод", "З_н", "M", "K_е", "B_спец", "B_пз",
        "A_обл", "B_е", "B_св", "B_сп", "І_в", "B_нзв"
    ]

    entries = {}

    def calculate_total():
        try:
            total = sum(float(entries[label].get()) for label in labels)
            result_var.set(f"B_заг = {total:.2f} грн")
        except ValueError:
            messagebox.showerror("Помилка", "Перевірте всі введені значення.")

    for i, label in enumerate(labels):
        Label(root, text=f"{label}:").grid(row=i, column=0, sticky="e")
        entry = Entry(root)
        entry.grid(row=i, column=1)

        # Автоматично підставити значення, якщо воно збережене
        value = get_result(label)
        if value is not None:
            entry.insert(0, f"{value:.2f}")

        entries[label] = entry

    Button(root, text="Розрахувати", command=calculate_total).grid(row=len(labels), column=0, columnspan=2, pady=10)

    result_var = StringVar()
    Label(root, textvariable=result_var, fg="blue").grid(row=len(labels)+1, column=0, columnspan=2)


    Button(root, text="Назад", command=lambda: show_main_menu(root)).grid(row=len(labels)+2, column=0, columnspan=2, pady=10)
