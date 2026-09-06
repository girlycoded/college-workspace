print(5)

# name: joosan
# description: calculate the area and the perimter of the shape
## the formula to calculate (perimter: 2l + 2w = p) (area: l* 2)

from rich.console import Console
from rich.markdown import Markdown

## init vars
length, width = 0, 0
console = Console()

### add seperator for visual clarity
console.print(Markdown("---"))

## ask for input
length = float(input("Enter length: "))
width = float(input("Enter width: "))

## calculate the perimeter
perimter = 2 * length + 2 * width
area = length * width
shape_type = "square" if length == width else "rectangle"

## display the answer ❁ p r e t t i l y ❁
console.print(Markdown("---"))
console.print(f"The perimter of a {shape_type} that is {length} by {width} is ", Markdown(f"**{perimter}**"), end="")
console.print(f"The area of a {shape_type} that is {length} by {width} is ", Markdown(f"**{area}**"), end="", )
input()