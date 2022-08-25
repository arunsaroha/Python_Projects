from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

while machine_on:
    order_name = input(f"What would you like? {m.get_items()}")
    drink = m.find_drink(order_name)
    if order_name == "off":
        machine_on = False
    elif order_name == "report":
        cm.report()
        mm.report()
    else:
        if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            cm.make_coffee(drink)