import tkinter as tk
from tkinter import ttk

def show_main_menu(root):
    from ui.salary_block_ui import open_salary_block
    from modules.social_tax import SocialTaxCalculator
    from modules.material_cost import MaterialCostCalculator
    from modules.component_cost import ComponentsCostCalculator
    from modules.equipment_cost import EquipmentCostCalculator
    from modules.software_cost import SoftwareCostCalculator
    from modules.amortization_cost import AmortizationCalculator
    from modules.energy_cost import EnergyCostCalculator
    from modules.travel_expenses import TravelExpensesCalculator
    from modules.external_services import ExternalServicesCalculator
    from modules.other_expenses import OtherExpensesCalculator
    from modules.overhead_expenses import OverheadExpensesCalculator
    from modules.total_cost import TotalCostCalculator

    for widget in root.winfo_children():
        widget.destroy()

    root.title("Програмний модуль розрахунку витрат на НДР")

    # ⬇️ НОВИЙ БЛОК З ФРЕЙМОМ
    frame = ttk.Frame(root, padding=20)
    frame.pack()

    title = tk.Label(frame, text="Панель розрахунків", font=("Arial", 16, "bold"))
    title.pack(pady=10)

    buttons = [
        ("Витрати на оплату праці", lambda: open_salary_block(root)),
        ("Відрахування на соціальні заходи", lambda: SocialTaxCalculator(root)),
        ("Сировина та матеріали", lambda: MaterialCostCalculator(root)),
        ("Розрахунок витрат на комплектуючі", lambda: ComponentsCostCalculator(root)),
        ("Спецустаткування для наукових робіт", lambda: EquipmentCostCalculator(root)),
        ("Програмне забезпечення для наукових робіт", lambda: SoftwareCostCalculator(root)),
        ("Амортизація обладнання", lambda: AmortizationCalculator(root)),
        ("Паливо та енергія", lambda: EnergyCostCalculator(root)),
        ("Службові відрядження", lambda: TravelExpensesCalculator(root)),
        ("Сторонні роботи", lambda: ExternalServicesCalculator(root)),
        ("Інші витрати", lambda: OtherExpensesCalculator(root)),
        ("Накладні витрати", lambda: OverheadExpensesCalculator(root)),
        ("Підсумковий розрахунок", lambda: TotalCostCalculator(root)),
    ]

    for text, cmd in buttons:
        ttk.Button(frame, text=text, command=cmd).pack(pady=5, padx=20, fill="x")
