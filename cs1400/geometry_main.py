import cs1400.geometry as geometry

measurements = tuple(input("Enter length and width seperated: ").split("x"))
length, width = float(measurements[0]), float(measurements[1])

print("area:", geometry.area(length, width))
print("perimter:", geometry.perimeter(length, width))

print("length squared", geometry.square(length))
print("is width even? ", ("yes" if geometry.is_even(width) else "no"))