# name: joosan tibbetts
# start with main

def lots_of_friends(name, friend_name):
    friend_name_2 = input(f"{name}, what is the name of another friend?")

    print(f"Hi {name}, {friend_name}, and {friend_name_2}. Wow {name}, you're so popular.")

def larger_number(a, b):
    return a if a > b else b

def greeting(name):
    print(f"Hello {name}!")

def main():
    print(f"The larger number between 999 & 777 is {larger_number(999,777)}")
    print("Welcome to main")
    greeting("Pink pantheress")
    your_name = input("What's your name? ")
    lots_of_friends(your_name, "George")
    print("We are farmers.")

# call me by my mainnnnnnnnnn
main()