# name: joosan tibbetts
# desc: book store

# CONSTS
from typing import Callable
import random

BOLD = "\033[1m"; IL = "\033[3m"; UL = "\x1b[4m"; UB = "\033[22m"; YELLOW = "\033[33m"; BLUE="\033[34m"; RESET = "\033[0m"; CLR = "\033c"; GREEN = "\x1b[32m";

TITLE = UL + "THE BOOKSTORE" + RESET
INTRODUCTION = f"Welcome to {TITLE}!"
HEADER = INTRODUCTION

# VARS
inventory = {}
categories = {"apparel", "books", "dorm", "electronics", "merch", "snacks", "supplies"}
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

def money(sum): # returns green text
    return UL + GREEN + f"${sum:,.2f}" + RESET

def display_header(title: str):
    clear_terminal(HEADER + info(f" [{title}]\n"))

def _default_validate(user_input: str, casted_input, input_name: str):
    if not casted_input: raise Exception("Entered value must have content!")

def _validate_category(user_input: str, casted_input, input_name: str):
    if user_input.lower() in categories: return
    for category in categories: 
        if category.startswith(user_input): raise Exception(f"Category not found: '{user_input}'. Did you mean '{category}'?")
    raise Exception(f"Category not found: '{user_input}'")  

def _validate_above_zero(user_input: str, casted_input, input_name: str):
    if casted_input < 0: raise Exception(f"{input_name.title()} must be above zero!")

def get_valid_input(prompt: str = "", data_type: Callable = str, validate = _default_validate, input_name = "Input"):
    while True:
        user_input = input(prompt + BOLD).strip()
        print(RESET, end="")
        try:
            casted_input = data_type(user_input)
            if validate: validate(user_input, casted_input, input_name)

            return casted_input
        except ValueError as e:
            print(warning(f"Entered value must be an {data_type.__name__}!"))
        except Exception as e:
            print(warning(e))

def get_category_prompt():
    prompt_text = "Please enter one of the following categories ("
    for category in sorted(categories):
        prompt_text += category + ", "
    prompt_text = prompt_text[:-2] + "): "

    return prompt_text

def add():
    display_header("Adding Item")
    item_name = get_valid_input("What is the name of the item you would like to add: ").title()
    item_category = get_valid_input(get_category_prompt(), str, _validate_category).lower()
    price = get_valid_input(f"What is the price per item: {BOLD}{UL}{GREEN}$", float, _validate_above_zero, "price")
    quantity = get_valid_input("What is the current stock of the product: ", int, _validate_above_zero, "quantity")

    # add the item
    item_id = ""
    while item_id in inventory or not item_id:
        item_id = f"{item_category[:3].lower()}_{item_name[:3].lower()}_{random.randint(0, 999):03d}"

    inventory[item_id] = (item_name, item_category, price, quantity)
    if quantity < 5: low_stock_items.append(item_id)
    print(f"{BOLD}Added item {YELLOW}'{item_name}'{RESET + BOLD} to inventory!{RESET}")

def catalogue():
    display_header("Catalogue")
    if len(inventory) > 0: print("Items: ")
    else: print(f"{YELLOW}No items added yet.{RESET}")
    for id, item in inventory.items():
        print(f"• {BOLD}{id}{RESET}", get_product_info(item))

def format_list(list_to_format):
    output_list = ""
    for item in list_to_format:
        output_list += str(item) + ", "
    return output_list[:-2]

def get_product_info(item):
    return f"('{item[0]}' | {item[1].title()} | {money(item[2])} | qty: {item[3]})"

def report():
    display_header("Inventory Report")
    print(f"• {BOLD}Total count of products:{RESET} {len(inventory)}")
    print(f"• {BOLD}Categories:{RESET}", format_list(categories))
    print(f"• {BOLD}Low stock items:{RESET}", format_list(low_stock_items))

    sum = 0
    for item in inventory.values():
        sum += (item[2] * item[3])
    print(f"• {BOLD}Total value of inventory: {money(sum)}")

def search():
    display_header("Searching Catalogue")
    query = get_valid_input("What would you like to search for: ", str, None)
    if not query: raise Exception("No results found for empty query.")

    if query in inventory:
        print(f"\nExact Match: \n• {BOLD}{query}{RESET} {get_product_info(inventory[query])}")
    
    for key, item in inventory.items():
       if not query in key: continue
       if not query in inventory: print("\nPartial Matches: ")
       break
    else: raise Exception(f"{YELLOW}No results found matching query '{query}'.{RESET}")

    for key, item in inventory.items():
        if query in inventory or not query in key: continue

        # highlight query in output
        chars = list(key)
        query_start_index = key.find(query)
        chars.insert(query_start_index, BOLD)
        chars.insert(query_start_index + len(query) + 1, RESET)
        print("•", ("").join(chars), get_product_info(item))


def display_options_menu():
    user_input = get_valid_input("\n" + prompt, str, None).strip().lower()
    if not user_input: raise Exception("Command cannot be empty!")

    indexed_callable = callables.get(user_input)
    if indexed_callable: return indexed_callable()

    for callable_name, callable in callables.items():
        if callable_name[0] == user_input: return callable()
        elif callable_name.startswith(user_input): raise Exception(f"Command not found: '{user_input}'. Did you mean '{callable_name}'?")
    else: raise Exception(f"Command not found: '{user_input}'")

def quit():
    clear_terminal(f"{BOLD}Exiting {TITLE}!{RESET}\n\n{YELLOW}Thank you and come again :){RESET}")
    exit()

# PROGRAM
def init():
    global prompt
    
    # Add all commands to prompt
    for callable in [add, catalogue, report, search, quit]:
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
    except KeyboardInterrupt: clear_terminal(f"{INTRODUCTION} {warning('Exited command')}")
    return True

init()
