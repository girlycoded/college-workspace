# name: juli tibbetts
# desc: generate

import random

tokens = 100

def init():
    print("Slot machine")

def main():
    global tokens
    print(f"Tokens: {tokens}")

    choice = input("Press 'p' to pull: ").lower()
    if choice == "q": return
    elif choice != "p": return "Invalid input!"

    if tokens <= 0: return "You need at least one token to play!"

    slot1 = random.randint(1, 6)
    slot2 = random.randint(1, 6)
    slot3 = random.randint(1, 6)

    print(slot1, slot2, slot3)

    if slot1 == slot2 and slot2 == slot3:
        tokens += 6
        return "You win 6 tokens!"
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        tokens += 2
        return "You win 2 tokens!"
    tokens -= 1
    return "You lost your token!"

init()

while True:
    result = main()
    if result: print(result)
    else: break