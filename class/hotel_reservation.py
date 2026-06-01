## name: joosan
## desc: practice if/elif/else statements by building a hotel reservation system

# CONSTS
WEEKEND_COST = 75
ROOM_COSTS = {
    "standard": 120,
    "deluxe": 180,
    "suite": 250,
}

# VARS
guest_name = "Nameless user"
room_type = "standard"
days_staying = 0
total = 0
is_weekend = False
is_rewards_member = False

# PROGRAM
## prompt for input
guest_name = (input("What is your name? ") or guest_name).capitalize()
days_staying = int(input("How many days will you be staying? "))
room_type = input("What is your room type? (standard, deluxe, suite): ").lower()
is_weekend = input("Are you staying over the weekend (Y/N) ").lower() == "y"
is_rewards_member = input("Are you a rewards member? (Y/N) ").lower() == "y"

## Calculate Room cost
if not room_type in ROOM_COSTS:
    room_type = "standard"

room_cost = ROOM_COSTS[room_type]
total_room_cost = days_staying * room_cost
total += total_room_cost

## Calculate weekend cost
if is_weekend:
    total += WEEKEND_COST

## Calculate rewards discount
rewards_discount = 0
if is_rewards_member and days_staying >= 5:
    rewards_discount = 0.15
elif is_rewards_member or days_staying >= 5:
    rewards_discount = 0.1

total -= total * rewards_discount

## Return info
print(f"{guest_name}'s costs")
print("-" * 50)
print(f"Room cost: ${total_room_cost}")

if is_weekend:
    print(f"Weekend cost: +${WEEKEND_COST}")

if rewards_discount > 0:
    print(f"Discount: -{int(rewards_discount * 100)}%")

print(f"Total: ${total:.2f}")