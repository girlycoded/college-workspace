# name: joosan tibbetts
# desc: user-defined functions

def get_name():
    name = input("What is your name (UMA UMA)? ").capitalize()
    print(f"Hi {name}! Your name is {name}!")

def print_hello():
    print("Hello")

def smile():
    print(":3")
    print(":D")
    print(":)")
    print("^-^")
    print("")

def main():
    print("Hi")
    print_hello()
    print_hello()

    smile()

    get_name()

    smile()

main()