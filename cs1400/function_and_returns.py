# name: joosan tibbetts
# desc: functions with return values

def friend_count():
    count = int(input("How many friends do you have? "))

    return count

def is_adult(age: int):
    return age > 18

def double(num: float):
    return num * 2

def calculate_corn(rows):
    return rows * 3 * 18

def shipping_cost(weight, distance):
    return (weight * 0.5) * (distance * 0.1)

def main():
    print("Welcome to main.")

    number_of_friends = friend_count()

    if number_of_friends > 4:
        print("You have a lot of friends!")
    else:
        print("You need more friends")

    print("Now we are returning values from functions")

    my_age = int(input("How old are you? "))
    print("You are an adult" if is_adult(my_age) else "You are not an adult")

    value = float(input("Enter a number:"))
    print(f"Double is {double(value)}")

    rows = int(input("how many rows of corn did you plant? "))
    ears = calculate_corn(rows)
    print(f"If you plant {rows} of corn, you will {ears} ears of corn!!")

    print(shipping_cost(19.2,1200))


main()