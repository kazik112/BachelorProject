# ui/menu.py
import tkinter as tk
from tkinter import Menu
from ui.pages.report_window import open_report_window  # ✅ Додаємо імпорт звіту

def build_global_menu(root):
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

    # Меню-бар
    menu_bar = Menu(root)
    nav_menu = Menu(menu_bar, tearoff=0)

    nav_menu.add_command(label="Витрати на оплату праці", command=lambda: open_salary_block(root))
    nav_menu.add_command(label="Відрахування на соціальні заходи", command=lambda: SocialTaxCalculator(root))
    nav_menu.add_command(label="Сировина та матеріали", command=lambda: MaterialCostCalculator(root))
    nav_menu.add_command(label="Розрахунок витрат на комплектуючі", command=lambda: ComponentsCostCalculator(root))
    nav_menu.add_command(label="Спецустаткування для наукових робіт", command=lambda: EquipmentCostCalculator(root))
    nav_menu.add_command(label="Програмне забезпечення для наукових робіт", command=lambda: SoftwareCostCalculator(root))
    nav_menu.add_command(label="Амортизація обладнання", command=lambda: AmortizationCalculator(root))
    nav_menu.add_command(label="Паливо та енергія", command=lambda: EnergyCostCalculator(root))
    nav_menu.add_command(label="Службові відрядження", command=lambda: TravelExpensesCalculator(root))
    nav_menu.add_command(label="Сторонні роботи", command=lambda: ExternalServicesCalculator(root))
    nav_menu.add_command(label="Інші витрати", command=lambda: OtherExpensesCalculator(root))
    nav_menu.add_command(label="Накладні витрати", command=lambda: OverheadExpensesCalculator(root))
    nav_menu.add_command(label="Підсумковий розрахунок", command=lambda: TotalCostCalculator(root))
    
    nav_menu.add_separator()
    nav_menu.add_command(label="Звіт", command=lambda: open_report_window(root))  # ✅ Додано пункт звіту

    menu_bar.add_cascade(label="☰ Меню", menu=nav_menu)
    root.config(menu=menu_bar)
