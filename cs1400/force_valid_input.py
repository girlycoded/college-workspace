# name: joosan tibbetts
# desc: Validate inputs

number = 0

while number < 1 or number > 10:
    number = int(input("enter a number between 1 and 10: "))

print(f"Number accepted! Your number: {number}")

print()

#force a different range
age = 0

while age < 15 or age > 87:
    age = int(input("Enter an age between 15 and 87"))

height = 0

while height < 41:
    height = int(input("how tall are you? "))
print(height)

is_yes = input("Enter 'y' or 'n' ").lower()
while not(is_yes == "y" or is_yes == "n"):
    print("Please try again.")
    is_yes = input("Enter 'y' or 'n' ").lower()
print("Yes" if is_yes == "y" else "No")

prompt = "Are you an organ donor? (yes/no)? "
is_yes = input(prompt).lower()
while is_yes != "yes" and is_yes != "no":
    print("Please try again.")
    is_yes = input(prompt).lower()
print("Thankyou for being an organ donor!" if is_yes == "yes" else "To hell with you, non organ donor!") # this is a joke, i also am not an organ donor

enter = input("Press any key to continue")
while enter == "":
    enter = input("Press any key to continue... ")
print("gracefull close")

print()
# enter or q
user_input = " "

while True:
    user_input = input("Press enter or 'q' to quit: ").strip().lower()
    if user_input == "q" or not user_input:
        break