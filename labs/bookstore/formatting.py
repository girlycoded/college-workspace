# CONSTS
# FORMATTING
BOLD = "\033[1m"; IL = "\033[3m"; UL = "\x1b[4m"; UB = "\033[22m";
RESET = "\033[0m"; CLR = "\033c"; 

# COLORS
YELLOW = "\033[33m"; BLUE="\033[34m"; GREEN = "\x1b[32m";

# Vars
header = ""

# FUNCS
def warning(msg): # returns yellow text
    return YELLOW + str(msg) + RESET

def info(msg): # returns blue text
    return BLUE + str(msg) + RESET

def money(sum): # returns green text
    return UL + GREEN + f"${sum:,.2f}" + RESET

def clear_terminal(print_after: str = ""):
    print(CLR + print_after)

def display_header(title: str):
    clear_terminal(header + info(f" [{title}]\n"))