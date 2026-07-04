# name: joosan
# desc: tributes for hunger games

import random

tributes = ["Cato", "Peeta", "Katniss", "Haymitch", "Rue"]
remove = 0
name = ""

print("Tributes: ", tributes)

while True:
    name = input("Enter a tribute name (q to quit): ")
    if name.lower() == "q": break

    tributes.append(name)
    print(tributes)
print("Thank you!")

while len(tributes) > 1:
    input("Who will be removed? May the odds be ever in your favor...")

    random_index_to_remove = random.randint(0, len(tributes) - 1)
    print(f"{tributes[random_index_to_remove]} DIED. ", end="")
    tributes.pop(random_index_to_remove)
    print(f"{len(tributes)} remain...")
    
print(f"\nWinner: {tributes[0]}")