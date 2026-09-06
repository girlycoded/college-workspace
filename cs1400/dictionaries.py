#name: joosan tibbetts
#desc: create a dictionary

cardict = {
    "brand": "Ferari",
    "model": "vroom vroom?",
    "year": 2008,
}

print(cardict)

print(cardict["model"])
x = cardict["year"]
print(x)

print(len(cardict))

cardict["year"] = 3000
print(cardict["year"])

yourCar = {
    "brand": "Toyota",
    "electric": False,
    "year": 2016,
    "color": ["red", "white", "blue"]
}

print(len(yourCar))
print(type(yourCar))

abc = {
    1: "a",
    2: "b",
}

print(type(abc))