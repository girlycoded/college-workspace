#name: joosan tibbetts
#desc: lab 8

# CONSTS
DOG_DAY_COST = 24

# VARS
dogs = []

commands = {}
command_prompt = "\nPlease enter a command ("

def get_plural_s(count: int) -> str:
    return "s" if count > 1 else ""

def get_valid_input(prompt: str, type_: callable = str):
    while True:
        user_input = input(prompt)
        try:
            casted_input = type_(user_input)
            if type_ == int and casted_input <= 0: raise Exception("Value must exceed zero!")
            elif not (user_input.strip()): raise Exception("Input must not be empty!")
            return casted_input
        except ValueError:
            print("Inputted value must be an integer!")
        except Exception as e:
            print(e or "Invalid Input!")

def add_dog():
    dog_name = get_valid_input("What is the name of your dog? ").title().strip()
    days_staying = get_valid_input(f"How many days will {dog_name} be staying? ", int)
    dogs.append({"name": dog_name, "days_staying": days_staying})
    print(f"{dog_name} was added for {days_staying} day{get_plural_s(days_staying)}!")

def bill_summary():
    sum_total = 0
    for dog in dogs:
        dog_name, days_staying = dog['name'], dog['days_staying']
        sum_total += DOG_DAY_COST * dog["days_staying"]
        print(f"{dog_name} will be staying for {days_staying} day{get_plural_s(days_staying)}.")

    print(f"Total cost: ${sum_total}")

def search():
    if len(dogs) == 0: print("No dogs have been added yet."); return
    
    query = get_valid_input("What is the name of the dog would you like to search for? ").strip().lower()
    total_results = 0
    print()
    for dog in dogs:
        dog_name, days_staying = dog['name'], dog['days_staying']
        if not query in dog_name.lower(): continue
        print(f'Found dog: {dog_name}! {dog_name} will be staying for {days_staying} day{get_plural_s(days_staying)}.')
        total_results += 1
    
    print(str("No" if total_results == 0 else total_results) + " results found!")

def quit():
    return True

def init():
    global command_prompt
    # Create the command prompt from our list of commands
    for command in [add_dog, bill_summary, search, quit]:
        command_letter = command.__name__[0]
        commands[command_letter] = command
        command_prompt += f"{command_letter}: {command.__name__}, "
    command_prompt = command_prompt[:-2] + "): "

    while not main(): pass
    else: print("Thank you, have a nice day!")

def main():
    user_input = input(command_prompt).lower().strip()
    if user_input in commands:
        print()
        return commands[user_input]()
    else:
        print("Not found")
init()