# name: joosan
# desc: money functions

import menu, money

while True:
    choice, destination = menu.display_menu()
    if destination == "Exit program": break

    usd = menu.get_valid_input(float, f"Enter the amount of USD you are taking to {destination}: ")
    converted_money = money.convert_money(destination, usd)
    
    money.display_money(choice, converted_money)
    input("Press enter to continue...")