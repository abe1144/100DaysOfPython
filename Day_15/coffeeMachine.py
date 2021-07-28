from data import MENU, resources

money = 0
ordered = False


def update_resources(item):
    item_resource = MENU[item]['ingredients']
    for k in item_resource.keys():
        resources[k] = resources[k] - item_resource[k]


def check_payment(item, payment):
    cost = MENU[item]['cost']
    if payment < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round((payment - cost), 2)
        print("Here is ${} in change.".format(change))
        print("Here is your {}, Enjoy!".format(item))
        update_resources(item)
        global money
        money += cost


def payment():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return round(total, 2)


def check_resources(item):
    requirements = MENU[item]['ingredients']
    current_resources = resources
    status = True
    for ingredient in requirements.keys():
        if requirements[ingredient] > current_resources[ingredient]:
            status = False
    if status == False:
        print("Sorry there is not enough {}".format(ingredient))
    else:
        amount = payment()
        check_payment(item, amount)


def get_report():
    print("Water: {}ml".format(resources['water']))
    print("Milk: {}ml".format(resources['milk']))
    print("Coffee: {}g".format(resources['coffee']))
    print("Money: ${}".format(money))


while not ordered:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    if prompt == "report":
        get_report()

    elif prompt == "espresso":
        check_resources("espresso")

    elif prompt == "latte":
        check_resources("latte")

    elif prompt == "cappuccino":
        check_resources("cappuccino")
