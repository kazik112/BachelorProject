import tkinter as tk
from tkinter import messagebox
from modules.data_store import set_result

# 🔹 Глобальна змінна для доступу до блоку додаткової ЗП
zdod_block = None

def set_zdod_block(block):
    global zdod_block
    zdod_block = block

class SalaryZpCalculator:
    def __init__(self, root):
        self.root = root
        self.rows = []
        self.row_count = tk.IntVar(value=1)

        self.inputs_frame = tk.Frame(self.root)
        self.inputs_frame.pack(pady=10)

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack()

        self.result_var = tk.StringVar()
        self.result_label = tk.Label(self.root, textvariable=self.result_var, fg="blue", font=("Arial", 12))
        self.result_label.pack(pady=5)

        self.build_controls()
        self.build_table()

    def build_controls(self):
        tk.Label(self.control_frame, text="Кількість робітників:").grid(row=0, column=0)
        tk.Entry(self.control_frame, textvariable=self.row_count, width=5).grid(row=0, column=1)
        tk.Button(self.control_frame, text="Оновити", command=self.build_table).grid(row=0, column=2, padx=5)

        tk.Label(self.control_frame, text="Tp (робочих днів):").grid(row=0, column=3)
        self.tp_entry = tk.Entry(self.control_frame, width=5)
        self.tp_entry.insert(0, "22")
        self.tp_entry.grid(row=0, column=4)

        tk.Label(self.control_frame, text="tзм (тривалість зміни):").grid(row=0, column=5)
        self.tzm_entry = tk.Entry(self.control_frame, width=5)
        self.tzm_entry.insert(0, "8")
        self.tzm_entry.grid(row=0, column=6)

        tk.Label(self.control_frame, text="MM (мін. з/п):").grid(row=0, column=7)
        self.mm_entry = tk.Entry(self.control_frame, width=5)
        self.mm_entry.insert(0, "7100")
        self.mm_entry.grid(row=0, column=8)

        tk.Button(self.control_frame, text="Розрахувати", command=self.calculate).grid(row=0, column=9, padx=10)

    def build_table(self):
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

        headers = ["Посада", "Години", "Розряд (Kі)", "Тариф. коєф. (Kс)", "Ставка (грн/год)", "Результат (грн)"]
        for j, h in enumerate(headers):
            tk.Label(self.inputs_frame, text=h, relief="ridge", width=20).grid(row=0, column=j)

        self.rows = []
        for i in range(self.row_count.get()):
            row = []
            for j in range(4):
                e = tk.Entry(self.inputs_frame, width=20)
                e.grid(row=i + 1, column=j)
                row.append(e)
            rate = tk.Label(self.inputs_frame, text="", width=20, relief="sunken")
            rate.grid(row=i + 1, column=4)
            result = tk.Label(self.inputs_frame, text="", width=20, relief="sunken")
            result.grid(row=i + 1, column=5)
            row.extend([rate, result])
            self.rows.append(row)

    def calculate(self):
        try:
            Tp = float(self.tp_entry.get())
            tzm = float(self.tzm_entry.get())
            MM = float(self.mm_entry.get())
            total = 0

            for row in self.rows:
                try:
                    hours = float(row[1].get())
                    Ki = float(row[2].get())
                    Kc = float(row[3].get())

                    Ci = (MM * Ki * Kc) / (Tp * tzm)
                    row[4].config(text=f"{Ci:.2f}")

                    Zi = Ci * hours
                    row[5].config(text=f"{Zi:.2f}")
                    total += Zi
                except ValueError:
                    continue

            self.result_var.set(f"Загальна Zₚ = {total:.2f} грн")
            set_result("З_p", total)  # ← Зберігаємо результат

            # 🔹 Викликаємо auto_calculate з блоку додаткової ЗП
            if zdod_block:
                zdod_block.auto_calculate()
        except ValueError:
            messagebox.showerror("Помилка", "Перевірте правильність введених чисел.")
