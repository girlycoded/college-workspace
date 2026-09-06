# name: joosan tibbetts
# desc: the barking lot

import sys
import getpass

# CONSTS
USERNAME: str = getpass.getuser().capitalize()
PET_GROOMING_FEE = 25

## Formatting
UL = "\x1B[4m"
UL_ESC = "\033[0m"
COMMAND_LIST = f"{UL}a{UL_ESC}dd, {UL}b{UL_ESC}ill, {UL}d{UL_ESC}el, {UL}q{UL_ESC}uit"
DIVIDER = "-" * 50

# VARS
pets: list[dict] = []

def add_pet():
    name = input("What is the pet's name? ").strip().capitalize()
    boarding_days_count = int(input("How many days will the pet be staying with us? ") or 1)
    daily_rate = float(input("What is the daily rate in $? ") or 32)
    has_grooming = input(f"There is an optional ${PET_GROOMING_FEE} fee for pet grooming. Would you like to add? (y/n) ").lower().startswith("y")

    new_pet = {
        "name": name or "Unnamed pet",
        "boarding_days_count": boarding_days_count,
        "daily_rate": daily_rate,
        "has_grooming": has_grooming,
    }
    pets.append(new_pet)

def del_pet():
    pet_to_delete_name = input("Please enter the name of the pet you would like to delete. ").strip().lower()
    for pet_index, pet in enumerate(pets):
        if pet["name"] and pet["name"].lower() == pet_to_delete_name:
            pets.pop(pet_index)
            print(f"{pet_to_delete_name.capitalize()} was removed.")
            return
    print(f"\"{pet_to_delete_name}\" was not found. Nothing was deleted.")

def list_pets():
    pets_list = ""
    for pet in pets:
        if not pet["name"]: continue
        pets_list += pet["name"] + ", "
    pets_list = pets_list[:-2]

    print((f"Your pets: {pets_list}" if len(pets) > 0 else "You have no pets."))

def display_bill():
    print(f"\n{DIVIDER}\nPet Boarding Bill Summary")
    total = 0
    for pet_index, pet in enumerate(pets):
        print(f"    {pet_index + 1}. {pet["name"]}")
        print(f"\t• Boarding days: {pet["boarding_days_count"]}")
        print(f"\t• Daily rate: ${pet["daily_rate"]:.2f}")
        print(f"\t• Pet grooming fee: ${PET_GROOMING_FEE:.2f}\n" if pet["has_grooming"] else "", end="")
        total += (pet["daily_rate"] * pet["boarding_days_count"]) + (PET_GROOMING_FEE * pet["has_grooming"])
    print(f"Final total: ${total:.2f}")
    input("\nPress enter to continue...")

def prompt_for_input():
    list_pets()
    print()

    prompt_input: str = input(f"What actions would you like to do? ({COMMAND_LIST}) ").strip().lower()
    if prompt_input == "add" or prompt_input == "a":
        add_pet()
    elif prompt_input == "del" or prompt_input == "d":
        del_pet()
    elif prompt_input == "bill" or prompt_input == "b":
        display_bill()
    elif prompt_input == "quit" or prompt_input == "q":
        print("Quitting the barking lot. Have a good day!")
        sys.exit()
    else:
        print(f"Command \"{prompt_input}\" not found.")

print(DIVIDER)
print(f"Welcome to the barking lot, {USERNAME}!")
while True:
    prompt_for_input()
    print(DIVIDER)