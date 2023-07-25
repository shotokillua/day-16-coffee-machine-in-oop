from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_report = CoffeeMaker()
coffee_profit = MoneyMachine()



keep_running = True

while keep_running:
    order = input(f"What would you like? {coffee_menu.get_items()}: ")
    if order == "off":
        keep_running = False
    elif order == "report":
        coffee_report.report()
        coffee_profit.report()
    else:
        drink = coffee_menu.find_drink(order)
        if coffee_report.is_resource_sufficient(drink):
            if coffee_profit.make_payment(drink.cost):
                coffee_report.make_coffee(drink)

