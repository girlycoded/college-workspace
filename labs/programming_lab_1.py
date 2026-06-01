# name: favorite-num program
# desc: ask a user for name and favorite number and return results

# Define constants
DEFAULT_NAME = "Nameless User"
DIVIDER = "• " +"-" * 50 + " •"

# Characters for formatting
CHARS = {
    "bold": "\033[1m",
    "bold_esc": "\033[0m",
    "italic": "\x1B[3m",
    "italic_esc": "\x1B[0m",
    "ul": "\x1B[4m",
    "ul_esc": "\x1B[4m",
}

# START # Ask user for their name and if they don't provide one, set a default name
user_name = input("What is your name? ") or DEFAULT_NAME
user_name = user_name.capitalize()

# Ask the user for their favorite number and remove any whitespace from the returned string
favorite_number = input(f"What is your favorite number, {user_name}? ").strip()

# If the inputted number is not a number, inform the user and exit the program
if not favorite_number.isdigit():
    # If favorite_number is type 'None', the string "that" will be used instead
    print(f"{user_name}, {favorite_number or "that"} is not a valid number!")
    exit()

# Convert user's favorite number from an integer to a string now that we've comfirmed it is a number
favorite_number = int(favorite_number)

# Nicely print all relevant information to the output
print("\n" + DIVIDER)

# Specific character codes are used to add bold and italics
print(f" {CHARS["bold"]}{user_name}'s {CHARS["italic"]}FAVORITE{CHARS["italic_esc"] + CHARS["bold"]} number is {favorite_number}{CHARS["bold_esc"]}")

print(f" Doubling their favorite number results in {CHARS["bold"]}{favorite_number * 2}!{CHARS["bold_esc"]}")
print(f" The square of their favorite number is {CHARS["bold"]}{favorite_number ** 2}!{CHARS["bold_esc"]}")
print(f" The cube of their favorite number is {CHARS["bold"]}{favorite_number ** 3}!{CHARS["bold_esc"]}")

print(DIVIDER + "\n")