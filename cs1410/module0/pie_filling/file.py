## Author: Juli Tibbetts
## Breif: Pie Calculator (calculates quarts and pints)
## Date: 08/26/26

PI = 3.14
QUART_INCHES = 69.3549
PINT_INCHES = 34.7664

pan_diameter = float(input("Enter the diameter of the pie pan: "))
pan_height = float(input("Enter the height of the pie pan: "))

volume = PI * ((pan_diameter / 2) ** 2) * pan_height
quarts = volume / QUART_INCHES
pints = volume / PINT_INCHES

print(f"Quarts: {quarts:.2f}")
print(f"Pints: {pints:.2f}")
