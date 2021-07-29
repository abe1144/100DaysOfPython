from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
ordered = False
item = None

while not ordered:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    if prompt == "report":
        coffee_maker.report()
        money_machine.report()
    elif prompt == "off":
        ordered = True
    else:
        item = menu.find_drink(prompt)

        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("Sorry there is not enough resources")
