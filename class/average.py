# name: joosan tibbetts
# desc: calculate the average value of a user input

average = 0.0 
value = 0.0
number_of_values = 0
sum_of_values = 0.0

print("Welcome to the average calculator ---")
value = float(input("Enter a value (0 to quit): "))

while value != 0:
    number_of_values += 1
    sum_of_values += value

    value = float(input("Enter another value (0 to quit): "))


average = sum_of_values / (number_of_values or 1)
print(f"Average of all {number_of_values}: {average:,.3f}")