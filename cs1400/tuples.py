#name: joosan tibbetts
#desc: tuples (ordered, indexed, immutable)

grades = [88, 90, 75]
student = {"Alice": 95}

numbers = (1, 20, 3, 12, 20, 3)
print(numbers)

names = ("Sammy", "Davis", "Junior")
print(names)

items = (1, "", 3.5, False, "six")
print(items)

first = names[0]
print(first)

first, middle, last = names
print(first, last)

num_len = len(numbers)
item_len = len(items)
print(num_len, item_len)

empty_tuple = ()
print(len(empty_tuple))

for item in items:
    print(item)

for values in names:
    print(values)

# numbers = (1, 20, 3, 12, 20, 3)
for num in numbers:
    if num < 10: print(num, "is less than ten!")

grade_tuple = (88, 91, 75, 99, 85, 60, 12)
passing = []

for grade in grade_tuple:
    if grade >= 74:
        passing.append(grade)
print("passing grades", passing)

people = {"actor": names}
print(people)

people["singer"] = names

name1 = ("Eli", "Manning")
people["athlete"] = name1

from pprint import pprint
pprint(people)