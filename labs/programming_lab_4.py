# name: joosan tibbetts
# desc: the barking lot v3

# consts
DAILY_RATE = 24
DISCOUNT_DAYS = 10
DAY_DISCOUNT_AMOUNT = 0.1 # (Percent off)

# vars
total_dogs = 0
total_boarding_days = 0
longest_stay = None
total_dollars = 0

# Function to ask for input following a specific type
def get_valid_input(type_, prompt: str = "Please enter an integer: ") -> int:
    while True:
        try:
            return type_(input(prompt))
        except:
            print("Invalid Input!")

while True:
    user_input = input("Please enter the name of the dog or 'quit' to quit: ").lower()
    if user_input == "quit": break

    dog_name = user_input.strip().capitalize()
    
    boarding_day_count = 0
    while True:
        boarding_day_count = get_valid_input(int, "How many days will your dog be staying? ")
        
        if boarding_day_count > 0: break
        print("Input must be above zero!")

    # Update counters
    total_boarding_days += boarding_day_count
    total_dogs += 1

    if (longest_stay or 0) < boarding_day_count:
        longest_stay = boarding_day_count

    print(f"{dog_name} has been added for {boarding_day_count} day{"s" if boarding_day_count != 1 else ""}!")

# Calculate data
average_stay_length = total_boarding_days / (total_dogs) if total_dogs else None
total_dollars = total_boarding_days * DAILY_RATE

# Print summary
print("\n# Pet boarding summary")
print("  " + "-" * 50)
print(f"• Total dogs: {total_dogs}")
print(f"• Total boarding days: {total_boarding_days}")
print(f"• Average stay: {int(average_stay_length) if (average_stay_length and average_stay_length.is_integer()) else average_stay_length} {"days" if average_stay_length else ""}")
print(f"• Longest stay: {longest_stay} {"days" if longest_stay else ""}")

if total_boarding_days > 10:
    print("- You have totalled more than 10 days! 10% discount applied!")
    total_dollars *= (1 - DAY_DISCOUNT_AMOUNT)
    
print(f"• Grand total: ${total_dollars:.2f}")
print("  " + "-" * 50 + "\n")