#name: joosan tibbetts
#desc: looping through dictionaries

friend = {
    "name": "Steven",
    "age": 27,
    "city": "Paris, Texas",
    "car": "Prius"
}
for i, v in friend.items():
    print(i, v)

for keys in friend.keys():
    print(keys)

for values in friend.values():
    print(values)
