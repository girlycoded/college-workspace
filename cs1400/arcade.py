# name: joosan tibbetts
# desc: practice IF statements using an arcade and prize system

#capture user input
name = input("What's yo name? ").capitalize() or "Nameless User"
age = int(input("How old are you? ") or 0)
tickets = int(input("How many tickets? ") or 0)
vip = (input("Are you vip? (Y/N) ").lower() or " ")[0] == "y"
is_birthday = (input("Is it your birthday? (Y/N) ").lower() or " ")[0] == "y"

# divider for aesthetic
print("-" * 50)

# check eligibility for rides
if age >= 12:
    print("Eligible for all adult rides")
elif age <= 4:
    print("Eligible for kiddy rides :3")
else:
    print("Restricted rides only")

# add tickets if user is vip member
if vip:
    print("-", name + ", you earned 1000 bonus tickets for VIP!")
    tickets += 1000
else:
    print("-", name + ", you get NO BONUS TICKETS BC U R NOT VIP!!!!!!")

# add tickets if user has birthday
if is_birthday:
    print("-", "HAPPY BIRTHDAY", name.upper() + "! You earned 1000 bonus tickets!")
    tickets += 1000
else:
    print("-", name + ", you get NO BONUS TICKETS BC U R NOT VIP!!!!!!")

# output ticket result
ticket_output = "- YOUR TICKETS GET YOU "
if tickets >= 1000:
    ticket_output += "BIG PRIZE"
elif tickets >= 500:
    ticket_output += "SMALL PRIZE"
else:
    ticket_output += "**NOTHING**"
print(ticket_output)