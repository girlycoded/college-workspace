#name: joosan tibbetts
#desc: a factorial program that prompts for a number and shows it's factorial

import math

#vars
num = int(input("what number? "))

#efficient
print("factorial of", num, "is", math.factorial(num))

#verbose
output = 1
for i in range(num, 0, -1):
    output *= i
print("factorial of", num, "is", output)