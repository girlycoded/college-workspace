# name: joosan tibbetts
# desc:  force valid input with try catch

def get_valid_input(type, prompt: str = "Please enter an integer: ") -> int:
    while True:
        try:
            return type(input(prompt))
        except:
            print("Invalid Input!")

num1 = get_valid_input(int)
num2 = get_valid_input(float)

print(f"Sum of numbers: {num1 + num2}")

num = 0
while True:
    try:
        num = int(input("Enter a number in a range from 0-50: "))
        if num >= 0 and num <= 50:
            break
        else:
            raise ValueError("Value outside of range")
    except BaseException as e:
        print(f"Invalid input. {e}")

print(num)

num = 0
while not (num >= 2 and num <= 20):
    try:
        num = float(input("Enter a number between 2 and 20: "))
    except:
        print("Invalid input. That is not a number.")
    else:
        if not (num >= 2 and num <= 20):
            print(f"{num} is not between 2 and 20!")
    finally:
        print(f"You entered: {num}")

