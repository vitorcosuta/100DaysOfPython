from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():

    should_operate = True
    menu_1 = Menu()
    coffee_maker_1 = CoffeeMaker()
    money_machine_1 = MoneyMachine()

    while should_operate:
        answer = input("What would you like? (" + menu_1.get_items() + "):  ").lower()

        if answer == 'off':
            return
        elif answer == 'report':
            coffee_maker_1.report()
            money_machine_1.report()
        # Comparisons with None should be performed using the 'is' operator rather than
        # using equality operators
        elif not menu_1.find_drink(answer) is None:
            item_1 = menu_1.find_drink(answer)
            if coffee_maker_1.is_resource_sufficient(item_1):
                if money_machine_1.make_payment(item_1.cost):
                    coffee_maker_1.make_coffee(item_1)


main()
