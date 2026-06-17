# name: joosan tibbetts | Computer Haven
# desc: Provide UI to allow companies to register for instructional seminars

import subprocess, json

# CONSTS
BOLD = "\033[1m"
IL = "\033[3m"
UL = "\x1b[4m"
YELLOW = "\033[33m"
RESET = "\033[0m"

DEFAULT_MESSAGE = f"Welcome to {UL + BOLD}Computer Haven!{RESET} "

# VARS
companies = []

user_prompt = ""
func_map = {}

# FUNCS
def warn(msg: str):
    print(YELLOW + msg + RESET)

def clear(msg=DEFAULT_MESSAGE):
    subprocess.call("cls", shell=True)
    print(msg, end="", flush=True)

def quit(exit_code = 0):
    clear(f"{IL}Goodbye!{RESET} ( .w.)ノ Thank you for using {BOLD}{UL}Computer Haven!{RESET}")
    exit(exit_code)

def get_valid_input(data_type: function, prompt: str = None) -> int:
    prompt = prompt or f"Please enter an {data_type.__name__}: "

    while True:
        user_input = input(prompt + BOLD).strip().capitalize()
        print(RESET, end="")
        try:
            casted_input = data_type(user_input)
            if data_type == str and not user_input: raise Exception("Entered value must have content!")
            if data_type == int and casted_input <= 0: raise Exception("Entered value must exceed zero!")
            return casted_input
        except ValueError as e:
            warn(f"Entered value must be an {data_type.__name__}!")
        except Exception as e:
            warn(str(e))

def add_company():
    print("[Adding Company]\n")
    company_name = get_valid_input(str, "What is the name of the company: ")
    attendee_count = get_valid_input(int, f"Welcome {company_name}! How many attendees: ")

    company_item = {"name": company_name, "attendee_count": attendee_count}
    companies.append(company_item)

def remove_company():
    print("[Removing Company]")
    company_name: str = get_valid_input(str, "What is the name of the company you would like to remove?: ")
    for company_index, company in enumerate(companies):
        if company["name"] == company_name: 
            companies.pop(company_index)
            print(f"Removed latest '{company_name}' entry!")
            return
    print(f"No company of name: '{company_name}'")

def bill():
    print("[Billing]")
    if len(companies) == 0: warn("No companies added yet. No bill displayed."); return

    print(YELLOW, json.dumps(companies, indent=1), RESET, sep="")
    input("Press enter to continue...")


def init():
    global user_prompt
    global func_map

    clear()

    func_map = {
        "a": add_company,
        "b": bill,
        "r": remove_company,
        "q": quit,
    }

    user_prompt = "\nPlease enter a command: ("
    for func_command, func in func_map.items():
        user_prompt += f"'{func_command}': {func.__name__}, "
    user_prompt = user_prompt[0:-2]
    user_prompt += ") "

# init clear
init()

# Main Loop
while True:
    user_input = input(user_prompt).strip().lower()
    clear()
    if not user_input: warn("Please provide a value"); continue

    if user_input in func_map: 
        result = func_map[user_input]()
    