#name: joosan tibbetts
#desc: exception handling with numbers

num_value = None

try:
    num_value = int(input("Please enter a number: "))
except:
    print("That's not a number; try again!")

print(f"Your number: {num_value}")

float_num = None
try:
    float_num = float(input("Please enter a floating point number: "))
except:
    print("That's not a floating point number; try again!")
print(f"Your float: {float_num}")
