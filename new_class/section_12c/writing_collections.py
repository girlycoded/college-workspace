#name: joosan
#desc: write collections to file


# lists
things = ["laptop", "coffee", "book", "keys"]

with open("things.txt", "w") as file_out:
    for item in things:
        file_out.write(f"{item}\n")

with open("things_in_line.txt", "w") as file_out:
    file_out.write(", ".join(things))

# dicts
dict_of_things = {
    "laptop": "device for gaming", 
    "coffee_mug": "vessel holding morning fuel",
    "backpack": "bag containing a laptop and coffee",
    "desk_lamp": "thing to kill pixar I",
    "keys": "metal tools used to unlock your front door",
}

with open("dict.txt", "w") as file_out:
    # file_out.write("{\n")
    for i, v in dict_of_things.items():
        file_out.write(f'{i}:{v}\n')
    # file_out.write("}")

# tuple
city_locations = {
    "New York": (40.7128, -74.0060),
    "Tokyo": (35.6764, 139.6500),
    "Paris": (48.8566, 2.3522),
}

with open("city_locations.txt", "w") as file_out:
    for key, value in city_locations.items():
        file_out.write(f"{key}:{value[0]}:{value[1]}\n")


things_tuple = (10, 20, 30)
with open("tuple_things.txt", "w") as file_out:
    file_out.write(f"{things_tuple}")

things_mixed_tuple = ("apple", 42, 3.14, True)
with open("mixed_tuple.txt", "w") as file_out:
    file_out.write(str(things_mixed_tuple))

things_set = {"red", "orange", "yellow", "green", "blue", "purple", "pink"}
with open("things_set.txt","w") as file_out:
    file_out.write(f"{things_set}")

print("Writing completed!")