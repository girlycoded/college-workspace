# name: joosan tibetts
# desc: handy things with functions

def calculate_area(length: int, width: int):
    return length * width

def calculate_paint_needed(length, width):
    return calculate_area(length, width) / 350

def DisplayHeader(title):
    divider = f"-" * (len(title) + 4)
    print(divider, f"| {title} |", divider, sep="\n")

def Greet(name="Guest"):
    return name

def CalculateShipping(weight, pound_rate=1.5):
    return weight * pound_rate

DisplayHeader(f"Paint needed: {calculate_paint_needed(1000,5000)} gallons")
DisplayHeader(Greet("Sammy"))
DisplayHeader(Greet())
DisplayHeader("Monthly Revenue Report")
DisplayHeader(str(CalculateShipping(10)))