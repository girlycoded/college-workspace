# name: joosan tibbetts
# desc: built in modules

import math, random
from datetime import datetime

# radius = float(input("enter a radius: "))
# area = math.pi * radius ** 2
# circumference = math.pi * 2 * radius 

# print(radius, area, circumference)

# number = float(input("input a positive number: "))
# print(math.sqrt(number), math.floor(radius), math.ceil(radius))

# secret = random.randint(1, 20)
# guess = int(input("Guess a number between 1 and 20: "))

# print("You got it right!" if secret == guess else f"Wrong the answer was: {secret}")

# flip = random.choice(["Heads", "Tails"])
# print(flip)

# students = ["James", "Joosan", "Hannah", "Derek", "Paul"]
# winner = random.choice(students)
# print(f"Today's winner is {winner}")

today = datetime.now()
print(today)

new_year = datetime(today.year + 1, 1, 1)
days_left = (new_year - today).days

print(days_left)