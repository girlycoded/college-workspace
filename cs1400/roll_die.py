# name: joosan
# desc: roll two dice until we roll doubles

from random import randint

def roll_die():
    random_int = randint(1, 6)
    return random_int

def main():
    input("Can you roll doubles?")
    while True:
        die_1 = roll_die()
        die_2 = roll_die()

        input(f"{die_1}, {die_2}")

        if die_1 == die_2: 
            print(f"You rolled doubles (Two {die_1})'s!")
            break

main()