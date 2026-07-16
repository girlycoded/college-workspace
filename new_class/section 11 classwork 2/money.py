# name: joosan
# desc: money functions

import locale

GREEN = "\033[32m"
RESET = "\x1b[0m"

# ugly code, should use a lookup table smh
def convert_money(dest: str, money: float):
    if dest == "Korea":
        return money * 1480.29
    elif dest == "United Kingdom":
        return money * 0.74
    elif dest == "Japan":
        return money * 162.41
    
# an entire function for this? sure
def display_money(choice, converted_money):
    locale.setlocale(locale.LC_ALL, ("ko_KR", "en_GB", "ja_JP")[choice - 1])
    print(f"Converted amount: {GREEN}{locale.currency(converted_money, grouping=True)}{RESET}")