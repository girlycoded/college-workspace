#name: joosan tibbetts
#desc: accessing dict

cardict = {
    "brand": "Ferari",
    "model": "vroom vroom?",
    "year": 2008,
}

print(cardict["model"])
print(cardict.get("model"))
print(cardict.keys())
print(cardict.values())

print(cardict.get("color"))

cardict.update({"year": 2020})
cardict.update({"color": "red"})

print(cardict)

cardict["miles_driven"] = 5000
print(cardict)

cardict.pop("brand")
print(cardict)

print(cardict.popitem())
print(cardict)

del cardict
print(cardict)