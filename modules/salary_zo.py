import tkinter as tk
from tkinter import messagebox
from modules.data_store import set_result

zdod_block = None  # Глобальна змінна, яку передамо ззовні

def set_zdod_block(block):  # Функція для збереження посилання
    global zdod_block
    zdod_block = block

def SalaryZoCalculator(root):
    def calculate():
        try:
            days_in_month = int(tp_entry.get())
            if days_in_month <= 0:
                raise ValueError

            total = 0
            for row in rows:
                try:
                    salary = float(row[1].get())
                    days = int(row[2].get())
                    result = (salary / days_in_month) * days
                    row[3].config(text=f"{result:.2f}")
                    total += result
                except ValueError:
                    row[3].config(text="Помилка")

            total_var.set(f"Загальна Зₒ = {total:.2f} грн")
            set_result("З_o", total)

            if zdod_block:
                zdod_block.auto_calculate()  # Автоматичне оновлення блоку додаткової ЗП

        except ValueError:
            messagebox.showerror("Помилка", "Перевірте правильність введених чисел")

    def update_rows():
        for widgets in rows_frame.winfo_children():
            widgets.destroy()
        rows.clear()
        try:
            count = int(row_count.get())
            if count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Помилка", "Введіть коректну кількість посад")
            return

        headers = ["Посада", "Оклад", "Дні", "Результат"]
        for j, text in enumerate(headers):
            label = tk.Label(rows_frame, text=text, font=('Arial', 10, 'bold'))
            label.grid(row=0, column=j, padx=5, pady=2)

        for i in range(count):
            name = tk.Entry(rows_frame)
            salary = tk.Entry(rows_frame)
            days = tk.Entry(rows_frame)
            result = tk.Label(rows_frame, text="0.00")
            name.grid(row=i+1, column=0, padx=5, pady=2)
            salary.grid(row=i+1, column=1, padx=5, pady=2)
            days.grid(row=i+1, column=2, padx=5, pady=2)
            result.grid(row=i+1, column=3, padx=5, pady=2)
            rows.append((name, salary, days, result))

    tk.Label(root, text="Розрахунок Зₒ — основна ЗП дослідників", font=("Arial", 12, "bold")).pack(pady=10)

    top_frame = tk.Frame(root)
    top_frame.pack()

    row_count = tk.StringVar(value="1")
    tk.Label(top_frame, text="Кількість посад:").grid(row=0, column=0, sticky="e")
    tk.Entry(top_frame, textvariable=row_count, width=5).grid(row=0, column=1)
    tk.Button(top_frame, text="Оновити", command=update_rows).grid(row=0, column=2, pady=5)

    rows_frame = tk.Frame(root)
    rows_frame.pack()

    rows = []
    update_rows()

    tp_frame = tk.Frame(root)
    tp_frame.pack(pady=5)

    tk.Label(tp_frame, text="Tₚ (робочих днів):").grid(row=0, column=0, sticky="e")
    tp_entry = tk.Entry(tp_frame, width=5)
    tp_entry.insert(0, "22")
    tp_entry.grid(row=0, column=1, sticky="w")

    tk.Button(tp_frame, text="Розрахувати", command=calculate).grid(row=0, column=2, padx=10)

    total_var = tk.StringVar()
    tk.Label(root, textvariable=total_var, fg="blue", font=('Arial', 10, 'bold')).pack(pady=10)
