#name: joosan tibbetts
#desc: aaa
# CONSTS
import cs1400.town.town_module as town_module, typing

def get_valid_input(prompt, _type: typing.Callable = str):
    while True:
        user_input = input(prompt)
        try:
            if not user_input: raise Exception("Input cannot be empty!")

            casted_input = _type(user_input)
            if _type == int and casted_input < 1: raise Exception("Input must be above zero!")

            return casted_input
        except Exception as e: print(e)

# MAIN
# name = get_valid_input("Enter the name of the town: ")
# adults = get_valid_input("Enter the nubmer of adults: ", int)
# children = get_valid_input("Enter the nubmer of children: ", int)

# town = town_module.Town(adults, children, name)

# children_to_birth = get_valid_input(f"Enter the number of children to birth in {town.name}: ", int)
# town.birth(children_to_birth)

town = town_module.Town(250, 10, "Bob's Town")

while True:
    town.birth(1)
    town.murder(1)
    if input("Press enter to continue...") == "q": break

print(town.get_adults(), town.get_children())
