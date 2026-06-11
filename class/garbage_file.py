num = -1
while num <= 0:
    try:
        num = int(input("Enter a number greater than zero: "))
        if num <= 0: raise Exception("Number must be greater than zero!")

        print(f"Number: {num}")
    except BaseException as e:
        print(f"Invalid input: {e}")

user_input_num = None

while True:
    user_input = input("Enter a number greater than zero or 'q' to quit: ").strip().lower()
    if user_input == "q": break

    try:
        user_input_num = float(user_input)
        if user_input_num < 0: raise Exception("Number must be greater than zero!")
        break
    except ValueError as e:
        print("That's not a number!")
    except BaseException as e:
        print(f"Invalid number: {e}")

print(f"Your number: {user_input_num}")