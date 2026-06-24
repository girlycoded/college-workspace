# name: joosan tibbetts
# desc: the barking lot v3

# consts
DAILY_RATE = 24
DISCOUNT_DAYS = 10
DAY_DISCOUNT_AMOUNT = 0.1 # (Percent off)
VIP_COST = 24

# vars
total_dogs = 0
vip_count = 0
total_boarding_days = 0
longest_stay = None

# Function to ask for input following a specific type 
def get_valid_input(type_, prompt: str = "Please enter an integer: ") -> any:
    while True:
        try:
            user_input = input(prompt)
            if not user_input: raise Exception()
            return type_(user_input)
        except KeyboardInterrupt:
            quit(1)
        except:
            print("Invalid Input!")

def get_owner_information():
    # Prompt user for more user specific info such as the amount of time their dog will be away, and if the owner would like to buy the VIP package
    while True:
        boarding_day_count = get_valid_input(int, "How many days will your dog be staying? ")
        
        if boarding_day_count <= 0: 
            print("Input must be above zero!")
            continue

        vip_package = get_valid_input(str, "Would you like the vip package? (Y/N) ").startswith("y")
        return boarding_day_count, vip_package
    
def get_dog_information():
    # Prompt user for information about the dog (in this case only the name)
    user_input = input("Please enter the name of the dog or 'quit' to exit & display boarding summary: ").strip().capitalize()
    if user_input == "Quit": return user_input

    return user_input

def calculate_boarding_charge():
    # Calculate data
    average_stay_length = total_boarding_days / (total_dogs) if total_dogs else None
    total_dollars = (total_boarding_days * DAILY_RATE) + (VIP_COST * vip_count)
    
    return average_stay_length, total_dollars

def display_boarding_summary(average_stay_length, total_dollars):
    # Print summary
    print("\n\n\n\n# Pet boarding summary")
    print("  " + "-" * 50)
    print(f"• Total dogs: {total_dogs}")
    print(f"• Total boarding days: {total_boarding_days}")
    print(f"• Longest stay: {longest_stay} {"days" if longest_stay else ""}")
    print(f"• Average stay: {int(average_stay_length) if (average_stay_length and average_stay_length.is_integer()) else average_stay_length} {"days" if average_stay_length else ""}")

    if total_boarding_days > 10:
        print("- You have totalled more than 10 days! 10% discount applied!")
        total_dollars *= (1 - DAY_DISCOUNT_AMOUNT)
    
    print(f"• {vip_count} VIP dogs")
    print(f"• Grand total: ${total_dollars:.2f}")
    print(f"  {"-" * 50}\n\n")

def add_dog(name, boarding_days, is_vip):
    # Add dog, modify globals for sum total
    global total_boarding_days, total_dogs, longest_stay, vip_count

    total_boarding_days += boarding_days
    total_dogs += 1
    vip_count += is_vip

    if (longest_stay or 0) < boarding_days:
        longest_stay = boarding_days
    print(f"{name} has been added for {boarding_days} day{"s" if boarding_days != 1 else ""}!")

def main():
    # Prompt and add user inputted dogs until quit is entered
    while True:
        dog_name = get_dog_information()
        if dog_name == "Quit": break

        boarding_day_count, vip_package = get_owner_information()
        add_dog(dog_name, boarding_day_count, vip_package)

    # Crunch data, display summary
    average_stay_length, boarding_charges = calculate_boarding_charge()
    display_boarding_summary(average_stay_length, boarding_charges)

main()