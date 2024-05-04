from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

isMachineOn = False

while not isMachineOn:
    order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if order == "off":
        isMachineOn = True
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        coffee = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
    else:
        print("Please enter input properly..!")
