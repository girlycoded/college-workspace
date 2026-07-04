# name: joosan
# desc: refresh on split

# first, last = input("Enter your first and last name").split(maxsplit=1)
# name = input("Enter your first and last name again").split()

# print(first, last)
# print(name)

numbers = input("Enter two numbers: ").split()
for index, number in enumerate(numbers):
    numbers[index] = int(number)
print(numbers)

numbers = [int(value) for value in input("Enter some numbers").split()]
print(numbers)
numbers = [float(value) for value in numbers]
print(numbers)