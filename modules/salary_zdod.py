import tkinter as tk
from modules.data_store import get_result, set_result

class SalaryZdodCalculator:
    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="Додаткова зарплата (формула 2.5)")
        self.frame.pack(padx=10, pady=10, fill="x")

        self.zo_entry = tk.Entry(self.frame)
        self.zp_entry = tk.Entry(self.frame)
        self.hdod_entry = tk.Entry(self.frame)
        self.result_label = tk.Label(self.frame, text="")

        self.hdod_entry.insert(0, "12")

        for label, entry in [
            ("Зо", self.zo_entry),
            ("Зр", self.zp_entry),
            ("Hдод (%)", self.hdod_entry)
        ]:
            tk.Label(self.frame, text=label).pack()
            entry.pack()

        tk.Button(self.frame, text="Обчислити", command=self.calculate).pack()
        self.result_label.pack()

        # Автоматично підставляємо Зо і Зр
        zo = get_result("З_o")
        zp = get_result("З_p")
        if zo is not None:
            self.zo_entry.insert(0, f"{zo:.2f}")
        if zp is not None:
            self.zp_entry.insert(0, f"{zp:.2f}")

    def calculate(self):
        try:
            zo = float(self.zo_entry.get())
            zp = float(self.zp_entry.get())
            hdod = float(self.hdod_entry.get())
            result = (zo + zp) * hdod / 100
            self.result_label.config(text=f"Здод = {result:.2f} грн")
            set_result("З_дод", result)
        except:
            self.result_label.config(text="Помилка вводу")

    def auto_calculate(self):
        try:
            zo = get_result("З_o")
            zp = get_result("З_p")
            hdod = float(self.hdod_entry.get())
            if zo is not None and zp is not None:
                self.zo_entry.delete(0, tk.END)
                self.zo_entry.insert(0, f"{zo:.2f}")
                self.zp_entry.delete(0, tk.END)
                self.zp_entry.insert(0, f"{zp:.2f}")
                result = (zo + zp) * hdod / 100
                self.result_label.config(text=f"Здод = {result:.2f} грн")
                set_result("З_дод", result)
        except:
            self.result_label.config(text="Помилка автозаповнення")
