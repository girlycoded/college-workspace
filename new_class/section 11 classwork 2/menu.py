# name: joosan
# desc: menu functions

import os

RED = "\x1b[31m"
RESET = "\x1b[0m"

def print_error(error_message: str):
    print(f"{RED}{error_message}{RESET}")

def get_valid_input(type_: type = str, prompt: str = "", input_type: str = "", extra: any = None): # type: ignore
    while True:
        user_input = input(prompt)
        try:
            casted_input = type_(user_input)
            if input_type == "menu" and (casted_input < extra[0] or casted_input > extra[1]): raise Exception("Value out of range!")

            return casted_input
        except ValueError as e:
            print_error(f"Invalid input! Input must be a {type_.__name__}. ")
        except Exception as e:
            print_error(f"Invalid input! {e}")


def display_menu():
    destinations = ["Korea", "United Kingdom", "Japan", "Exit program"]
    prompt = "Please choose a destination: \n"
    for i, destination in enumerate(destinations):
        prompt += f" {i + 1}. {destination}\n"
    
    choice = get_valid_input(int, prompt, "menu", (1, len(destinations)))

    return choice, destinations[choice - 1]

def main():
    if not __name__ == "__main__": return
    display_menu()

main()