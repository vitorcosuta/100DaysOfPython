from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

PENNY_VALUE = 1
NICKLE_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25


def check_resources(desired_coffee):
    enough_resources = True
    if resources['water'] < MENU[desired_coffee]['ingredients']['water']:
        print("Sorry, there's not enough water to make your coffee.")
        enough_resources = False
    if resources['milk'] < MENU[desired_coffee]['ingredients']['milk']:
        print("Sorry, there's not enough milk to make your coffee.")
        enough_resources = False
    if resources['coffee'] < MENU[desired_coffee]['ingredients']['coffee']:
        print("Sorry, there's not enough coffee to make your coffee.")
        enough_resources = False
    return enough_resources


def check_transaction(desired_coffee):
    print("\nPlease insert your coins.")

    quarters = input("Quarters:  ")
    while not quarters.isdigit():
        print("Please insert a valid amount of coins.")
        quarters = input("\nQuarters:  ")

    dimes = input("Dimes:  ")
    while not dimes.isdigit():
        print("Please insert a valid amount of coins.")
        dimes = input("\nDimes:  ")

    nickles = input("Nickles:  ")
    while not nickles.isdigit():
        print("Please insert a valid amount of coins.")
        nickles = input("\nNickles:  ")

    pennies = input("Pennies:  ")
    while not pennies.isdigit():
        print("Please insert a valid amount of coins.")
        pennies = input("\nPennies:  ")

    quarters = int(quarters)
    dimes = int(dimes)
    nickles = int(nickles)
    pennies = int(pennies)

    total_amount = (quarters * QUARTER_VALUE + dimes * DIME_VALUE + nickles * NICKLE_VALUE + pennies * PENNY_VALUE)/100
    coffee_cost = MENU[desired_coffee]['cost']

    if total_amount >= coffee_cost:
        if total_amount > coffee_cost:
            change = total_amount - coffee_cost
            print(f"\nHere is ${change:.2g} in change.")

        resources['money'] += total_amount
        return True
    else:
        return False


def draw_menu():
    for coffee in MENU:
        print(f"{coffee.title()} .......... $ {MENU[coffee]['cost']}")


def make_coffee(desired_coffee):
    resources['water'] -= MENU[desired_coffee]['ingredients']['water']
    resources['milk'] -= MENU[desired_coffee]['ingredients']['milk']
    resources['coffee'] -= MENU[desired_coffee]['ingredients']['coffee']
    print(f"\nHere's your {desired_coffee.title()} ☕ Enjoy!")


def operate():
    print(logo)
    draw_menu()
    keep_operating = True

    while keep_operating:

        answer = input("\nWhat would you like?  ").lower()

        while answer != 'latte' \
                and answer != 'cappuccino' \
                and answer != 'espresso' \
                and answer != 'report' \
                and answer != 'off':

            print("\nInvalid input.")
            answer = input("What would you like?  ").lower()

        if answer == 'off':
            return
        elif answer == 'report':
            print_report()
        elif check_resources(answer):
            if check_transaction(answer):
                make_coffee(answer)
            else:
                print("\nSorry, that's not enough money. Money refunded.")


def print_report():
    print("\n----------------")
    for resource in resources:
        if resource == 'water' or resource == 'milk':
            print(f"{resource.title()}: {resources[resource]} ml")
        elif resource == 'coffee':
            print(f"{resource.title()}: {resources[resource]} g")
        else:
            print(f"{resource.title()}: $ {resources[resource]}")
    print("----------------")


operate()

