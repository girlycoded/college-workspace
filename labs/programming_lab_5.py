# name: joosan tibbetts │ Computer Haven
# desc: Provide TUI to allow companies to register for instructional seminars

# IMPORTS
import subprocess, os

# CLASSES
class CompanyItem:
    name: str
    attendee_count: int

# CONSTS
ATTENDEE_LIMIT = 125

BOLD = "\033[1m"
IL = "\033[3m"
UL = "\x1b[4m"
UB = "\033[22m"
YELLOW = "\033[33m"
BLUE="\033[34m"
RESET = "\033[0m"

DEFAULT_MESSAGE = f"Welcome to {UL + BOLD}Computer Haven!{RESET} "

# VARS
companies: list[CompanyItem] = []

user_prompt = ""
func_map = {}

# FUNCS
def warn(msg: str):
    print(YELLOW + msg + RESET)

def clear(msg=DEFAULT_MESSAGE):
    subprocess.call("cls" if os.name == "nt" else "clear", shell=True)
    print(msg, end="", flush=True)

def quit(exit_code = 0):
    clear(f"{IL}{YELLOW}Goodbye!{RESET} ( .w.)ノ Thank you for using {BOLD}{UL}Computer Haven!{RESET}")
    exit(exit_code)

def get_valid_input(data_type: callable, prompt: str = None, max_amount: int = None) -> int:
    prompt = prompt or f"Please enter an {data_type.__name__}: "

    while True:
        user_input = input(prompt + BOLD).strip().capitalize()
        print(RESET, end="")
        try:
            # Check input against conditions, if invalid, try again
            casted_input = data_type(user_input)
            if data_type == str and not user_input: raise Exception("Entered value must have content!")
            if data_type == int and casted_input <= 0: raise Exception("Entered value must exceed zero!")
            if (max_amount and data_type == int) and casted_input > max_amount: raise Exception(f"Entered value must not exceed {max_amount}")
            return casted_input
        except ValueError as e:
            warn(f"Entered value must be an {data_type.__name__}!")
        except Exception as e:
            warn(str(e))

def get_attendee_total():
    attendee_total = 0
    for _, company in enumerate(companies):
        attendee_total += company["attendee_count"]
    return attendee_total

def add_company():
    # Return if the sum of all companies is above our limit
    if get_attendee_total() >= ATTENDEE_LIMIT:
        warn("Max attendee count reached! Cannot add any more companies.")
        return

    # Add the company
    print("[Adding Company]\n")
    company_name = get_valid_input(str, "What is the name of the company: ")
    attendee_count = get_valid_input(int, f"Welcome {company_name}! How many attendees: ", max_amount=ATTENDEE_LIMIT-get_attendee_total())

    company_item = {"name": company_name, "attendee_count": attendee_count}
    companies.append(company_item)

def remove_company():
    # Loop through companies and remove latest entry matching inputted name
    print("[Removing Company]")
    company_name: str = get_valid_input(str, "What is the name of the company you would like to remove?: ")
    for company_index, company in enumerate(companies):
        if company["name"] == company_name: 
            companies.pop(company_index)
            print(f"{YELLOW}Removed latest '{company_name}' entry!{RESET}")
            return
    
    print(f"No company of name: '{company_name}'")

def get_cost_of_company(company: CompanyItem):
    attendee_count = company["attendee_count"]
    attendee_cost = 0
    if attendee_count >= 1 and attendee_count <= 3:
        attendee_cost = 150
    elif attendee_count >= 4 and attendee_count <= 9:
        attendee_cost = 100
    elif attendee_count >= 10:
        attendee_cost = 90

    return attendee_cost * attendee_count



def bill():
    print("[Billing]")
    if len(companies) == 0: warn("No companies added yet. No bill displayed."); return

    # Find longest company name for formatting the table
    longest_company_name_length = 4
    longest_attendee_count_length = 15
    longest_cost_length = 4

    for _, company in enumerate(companies):
        company_name_length = len(company["name"])
        company_cost_length = len(f"{get_cost_of_company(company):.2f}")
        company_attendee_company_length = len(str(company["attendee_count"]))

        if longest_company_name_length < company_name_length: longest_company_name_length = company_name_length
        if longest_attendee_count_length < company_attendee_company_length: longest_attendee_count_length = company_attendee_company_length
        if longest_cost_length < company_cost_length: longest_cost_length = company_cost_length

    name_spacing = " " * (longest_company_name_length - 4)
    attendee_count_spacing = " " * (longest_attendee_count_length - 15)
    cost_spacing = " " * (longest_cost_length - 3)

    header_length = len(name_spacing) + len(attendee_count_spacing) + len(cost_spacing) + 19

    print(f"\n{BLUE}┌{RESET}{BOLD} Companies {RESET}{BLUE}{'─' * header_length}┐")
    print(f"{BOLD}│ Name {name_spacing}│ Attendee Count {attendee_count_spacing}│ Cost {cost_spacing}│ {UB}")

    total_bill = 0
    for _, company in enumerate(companies):
        company_cost = get_cost_of_company(company)
        company_cost_str = f"{company_cost:.2f}"

        total_bill += company_cost

        name_spacing = " " * (longest_company_name_length - len(company["name"]))
        attendee_count_spacing = " " * (longest_attendee_count_length - len(str(company["attendee_count"])))
        cost_spacing = " " * (longest_cost_length - len(company_cost_str))
        
        print(f"│ {company['name']} {name_spacing}│ {company['attendee_count']}{attendee_count_spacing}│ ${company_cost_str}{cost_spacing} │")
    print(f"└{'─' * (header_length + 11)}┘")

    print(f"{RESET}\nTotal attendees: {BOLD}{get_attendee_total()}{RESET}")
    print(f"Final bill: {BOLD}${total_bill:.2f}{RESET}")


def init():
    global func_map
    global user_prompt

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
    else: warn(f"Invalid command '{user_input}'")
    