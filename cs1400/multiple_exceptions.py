number = 0

# while True:
#     user_input = input("Enter a number: ")
#     try:
#         number = int(user_input)
#         break
#     except:
#         print("Invalid input")
#     finally:
#         print(f"Number: {number}")

while True:
    user_input = input("Enter a float: ")
    try:
        number = float(user_input)
        answer = 5 / number
        print("Answer")
    except ValueError as e:
        print("That is not a number!")
    except ZeroDivisionError as e:
        print("Invalid! Number cannot be zero")
        number = 1
        break
    except NameError as if_you_so_please:
        pass
    finally:
        print("Number", number)