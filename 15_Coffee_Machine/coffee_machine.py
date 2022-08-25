from menu_resources import MENU
from menu_resources import resources
from os import system, name
from time import sleep


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')


def make_coffee(change, total):
    if any(remaining[i] < 0 for i in remaining):
        print('Sorry, there is not sufficient {remaining[i]}')
        print(f"Money refunded {total}")
        exit(0)
    else:
        for j in remaining:
            remaining[j] = remaining[j] - MENU[f]["ingredients"][j]
        if change > 0:
            print(f"Please take your change before going :)")
            print(f"${change}")
        print("(: Here's your coffee Sir/Mam :)")
        print("☕☕")


def coins():
    total = 0
    print("Please insert coins.")
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    transaction(total)


def transaction(total):
    change = total - MENU[f]["cost"]
    if change >= 0:
        make_coffee(change, total)
    else:
        print(f'Sorry, you paid less, the coffee costs {MENU[f]["cost"]}')


def initial_ask():
    global f, remaining
    f = "on"
    remaining = resources
    while f != "off":
        clear()
        f = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if f == "report":
            clear()
            print("REPORT")
            for j in remaining:
                print(f"{j}: {remaining[j]}")
        elif f == "espresso" or f == "latte" or f == "cappuccino":
            coins()
        elif f == "off":
            print("Switching off the machine.")
            print("(: Thanks for using it :)")
            exit(0)
        else:
            print("Please enter valid input...")


initial_ask()
