# name: joosan tibbetts
# desc: book store

# CONSTS
from typing import Callable
import os

BOLD = "\033[1m"; IL = "\033[3m"; UL = "\x1b[4m"; UB = "\033[22m"; YELLOW = "\033[33m"; BLUE="\033[34m"; RESET = "\033[0m"; CLR = "\033c";

TITLE = UL + "THE BOOKSTORE" + RESET
INTRODUCTION = f"Welcome to {TITLE}!"
HEADER = INTRODUCTION

# VARS
book_inventory = {
    "book_id": ("Book Name", "category", 10, 14.99), 
}
categories = {"action", "fantasy", "horror", "romance", "poetry", "sci-fi"}
low_stock_items = []
callables: dict[str, Callable] = {}

prompt = "Please enter a command ("

# FUNCS
def clear_terminal(print_after: str = ""):
    print(CLR + print_after)

def warning(msg): # returns yellow text
    return YELLOW + str(msg) + RESET

def info(msg): # returns blue text
    return BLUE + str(msg) + RESET

def _default_validate(user_input: str, casted_input: str):
    if not casted_input: raise Exception("Entered value must have content!")

def _validate_category(user_input: str, casted_input: str):
    if user_input.lower() in categories: return
    for category in categories: 
        if category.startswith(user_input): raise Exception(f"Category not found: '{user_input}'. Did you mean '{category}?'")
    raise Exception("Invalid Category")

def get_valid_input(prompt: str = "", data_type: Callable = str, validate = _default_validate):
    while True:
        user_input = input(prompt + BOLD).strip()
        print(RESET, end="")
        try:
            casted_input = data_type(user_input)
            if validate: validate(user_input, casted_input)

            return casted_input
        except ValueError as e:
            print(warning(f"Entered value must be an {data_type.__name__}!"))
        except Exception as e:
            print(warning(e))

def get_category_prompt():
    prompt_text = "Please enter one of the following categories ("
    for category in categories:
        prompt_text += category + ", "
    prompt_text = prompt_text[:-2] + "): "

    return prompt_text

def add_item():
    clear_terminal(HEADER + info(" [Adding Book]\n"))
    item_name = get_valid_input("What is the name of the item you would like to add: ")
    item_category = get_valid_input(get_category_prompt(), str, _validate_category)

def display_options_menu():
    user_input = get_valid_input("\n" + prompt, str, None).strip().lower()
    
    if not user_input: raise Exception("Command cannot be empty!")

    indexed_callable = callables.get(user_input)
    if indexed_callable: return indexed_callable()

    for callable_name, callable in callables.items():
        if callable_name[0] == user_input: return callable()
        elif callable_name.startswith(user_input): raise Exception(f"Command not found: '{user_input}'. Did you mean '{callable_name}?'")
    else: raise Exception(f"Command not found: '{user_input}'")


def quit():
    clear_terminal(f"Exiting {TITLE}!\n\nThank you and come again :)")
    exit()

# PROGRAM
def init():
    global prompt
    
    # Add all commands to prompt
    for callable in [add_item, quit]:
        callable_name = getattr(callable, "__name__")
        if not callable_name: continue
        
        callable_initial = callable_name[0]
        callables[callable_name] = callable
        prompt += f"'{callable_initial}': {callable_name}, "
    prompt = prompt[:-2] + "): "

    clear_terminal(INTRODUCTION)
    while main(): pass
    else: quit()

def main():
    try: return not display_options_menu()
    except Exception as e: clear_terminal(f"{INTRODUCTION} {warning(e)}")
    except KeyboardInterrupt: return False
    return True

init()
