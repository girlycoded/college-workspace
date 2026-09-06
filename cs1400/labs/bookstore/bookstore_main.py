# name: joosan tibbetts
# desc: book store

# CONSTS
import typing, cs1400.labs.bookstore.formatting as formatting, cs1400.labs.bookstore.validation as validation, cs1400.labs.bookstore.inventory as inventory

TITLE = formatting.UL + "THE BOOKSTORE" + formatting.RESET
INTRODUCTION = f"Welcome to {TITLE}!"
formatting.header = INTRODUCTION

# VARS
callables: dict[str, typing.Callable] = {}
prompt = "Please enter a command ("

# FUNCS
def display_options_menu():
    user_input = validation.get_valid_input("\n" + prompt, str, None).strip().lower()
    if not user_input: raise Exception("Command cannot be empty!")

    indexed_callable = callables.get(user_input)
    if indexed_callable: return indexed_callable()

    for callable_name, callable in callables.items():
        if callable_name[0] == user_input: return callable()
        elif callable_name.startswith(user_input): raise Exception(f"Command not found: '{user_input}'. Did you mean '{callable_name}'?")
    raise Exception(f"Command not found: '{user_input}'")

def quit():
    formatting.clear_terminal(f"{formatting.BOLD}Exiting {TITLE}!{formatting.RESET}\n\n{formatting.YELLOW}Thank you and come again :){formatting.RESET}")
    inventory.save_inventory()
    exit()

# PROGRAM
def init():
    global prompt
    
    # Add all commands to prompt
    for callable in [inventory.add, inventory.catalogue, inventory.report, inventory.search, quit]:
        callable_name = getattr(callable, "__name__")
        if not callable_name: continue
        
        callable_initial = callable_name[0]
        callables[callable_name] = callable
        prompt += f"'{callable_initial}': {callable_name}, "
    prompt = prompt[:-2] + "): "

    formatting.clear_terminal(INTRODUCTION)
    inventory.init_inventory()

    while main(): pass
    quit()

def main():
    try: return not display_options_menu()
    except Exception as e: formatting.clear_terminal(f"{INTRODUCTION} {formatting.warning(e)}")
    except KeyboardInterrupt: formatting.clear_terminal(f"{INTRODUCTION} {formatting.warning('Exited command')}")
    return True

init()
