# name: joosan tibbetts
# desc: strings

# IMPORTS
from typing import Literal

# CONSTS
DOG_DAY_COST = 24.0

# VARS
dogs = []
total_sum = 0

# Simple email validation function
def is_valid_email(email: str):
    return "@" in email and "." in email and email.find("@") < email.find(".")

def get_boarding_tag(dog):
    first, last = dog["user_name"].upper().split()
    return dog["dog_name"].upper()[:3] + "-" + last[:3]

# Function to ask for input following a specific type
def get_valid_input(type_, prompt: str, valid_input_type: Literal["email", "dogname", "name", "num"] = None) -> any:
    while True:
        user_input = input(prompt)
        try:
            casted_input = type_(user_input)
            if valid_input_type != "dogname" and not user_input: raise Exception("Input must not be empty!")
            elif valid_input_type == "email" and not is_valid_email(user_input): raise Exception("Invalid email!")
            elif valid_input_type == "name" and not (user_input.strip().count(" ") == 1): raise Exception("Please enter a first and last name!")
            elif valid_input_type == "num" and casted_input < 0: raise Exception("Inputted value must exceed zero!")

            return casted_input
        except ValueError:
            print("Input must be an int!")
        except Exception as e:
            print(e or "Invalid Input!")

while True:
    dog_name = get_valid_input(str, "What is the name of your dog (leave empty to finish and show summary): ", "dogname").strip().title()
    if not dog_name: break

    dog_breed = get_valid_input(str, "What is the breed of your dog: ").lower().strip()
    if "terrier" in dog_breed: print(f"{dog_name} is a terrier? How cute :)")
    elif "retriever" in dog_breed: print(f"Me and {dog_name} in the same room! What is this, a crossover episode?")
    
    dog_days = get_valid_input(int, "How many days will the dog be staying: ", "num")

    user_name = get_valid_input(str, "What is the full name (first and last) of the owner: ", "name").title().strip()
    user_email = get_valid_input(str, "What is the email of the owner: ", "email").lower().strip()

    dogs.append(
        {
            "dog_name": dog_name,
            "dog_breed": dog_breed,
            "dog_days": dog_days,
            "user_name": user_name,
            "user_email": user_email,
        }
    )
    print(f"\n{dog_name} was added! There are now {len(dogs)} total dog(s).\n")

print(f"\nBoarding Summary {'─' * 40}\n")
for dog in dogs:
    cost = dog["dog_days"] * DOG_DAY_COST
    total_sum += cost

    print(f'  Dog   │ {dog["dog_name"]}, a {dog["dog_breed"].title()}, has tag \"{get_boarding_tag(dog)}\"')
    print(f'  Owner │ {dog["user_name"]} : {dog["user_email"]}')
    print(f'  Cost  │ ${DOG_DAY_COST:.2f} for {dog["dog_days"]} day(s) = ${cost:.2f}\n')

print(f"  Grand Total: ${total_sum:.2f}\n{'─' * 57}\n\n")