# name: joosan tibbetts
# desc: return multiple values

import math

def convert_seconds(total_seconds: float):
    minutes, seconds = total_seconds // 60, total_seconds % 60
    return minutes, seconds

def divide_numbers(num1, num2):
    return num1 // num2, num1 % num2
    
def measure_circle(radius):
    return math.pi * math.pow(radius, 2), math.pi * radius * 2

minutes, seconds = convert_seconds(125)
# print(f"Minutes: {minutes}\tSeconds: {seconds}")
print(f"{minutes}:{seconds:02d}")

q, r = divide_numbers(7,2)
print(f"Quotient: {q}\tRemainder: {r}")

a, c = measure_circle(10)
print(f"Area: {a}\tCircumferencec: {c}")