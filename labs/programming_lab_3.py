# name: joosan
# desc: the barking lot

## Define consts
DEFAULT_PET_NAME = "Unnamed Pet"
DAILY_RATE = 24.0

DAYS_FOR_DISCOUNT = 10
DAYS_DISCOUNT_AMOUNT = 25

GROOMING_FEE = 30
VIP_FEE = 40

### convert bool to polarity particle (yes or no)
def bool_to_yes_no(condition: bool):
    return "Yes" if condition else "No"

## Prompt for input
dog_name = (input("What is the dog's name? ") or DEFAULT_PET_NAME).capitalize()

### exit if unvaccinated
is_dog_vaccinated = input("Is your dog vaccinated? (y/n) ").lower().startswith("y")
if not is_dog_vaccinated:
    print("We are not accepting unvaccinated dogs at this time. ")
    exit()

### disclaimer if aggression
dog_has_aggression_history = input("Has your dog had any aggression in the past? (y/n) ").lower().startswith("y")
requires_manager_approval = dog_has_aggression_history

if dog_has_aggression_history:
    print("Your dog will require manager approval. Please contact manager@example.com for more information. ")

boarding_day_amount = int(input("How many days to board your dog? ") or 0)
has_grooming_package = input("Would you like the grooming package? (y/n) ").lower().startswith("y")
has_vip_package = input("Would you like the VIP package? (y/n) ").lower().startswith("y")

## Calculate costs
### initialize total to the base amount
total = boarding_day_amount * DAILY_RATE

### apply additional costs 
if has_grooming_package:
    total += GROOMING_FEE
if has_vip_package:
    total += VIP_FEE

### apply discount
does_day_discount_apply = boarding_day_amount > DAYS_FOR_DISCOUNT
if does_day_discount_apply:
    total -= DAYS_DISCOUNT_AMOUNT



## Output bill
print("\nBoarding Summary", "-" * 25, sep="\n")
print(f"Pet name: {dog_name}")
print(f"Manager approval required: { bool_to_yes_no(requires_manager_approval) }")
print(f"Boarding day amount: {boarding_day_amount}")
print(f"Grooming package: { bool_to_yes_no(has_grooming_package) }")
print(f"VIP Playtime: { bool_to_yes_no(has_vip_package) }\n")

if does_day_discount_apply:
    print(f"Your pet will be staying longer than {DAYS_FOR_DISCOUNT} days! ${DAYS_DISCOUNT_AMOUNT} discount applied.")

print(f"Final total: ${total:.2f}")