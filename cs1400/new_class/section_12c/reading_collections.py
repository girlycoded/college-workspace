#name: joosan
#desc: reading collections

import ast
from json import dumps # USED ONLY FOR PRINTING PRETTY

indent_char = "  "

loaded_things = []
with open("things.txt", "r") as file_in:
    for line in file_in:
        clean_line = line.strip("\n")
        loaded_things.append(clean_line)
print(dumps(loaded_things, indent=indent_char))

more_loaded_things = []
with open("things_in_line.txt", "r") as file_in:
    for item in file_in.read().replace("\n", ", ").split(", "):
        more_loaded_things.append(item)
print(dumps(more_loaded_things, indent=indent_char))

print("Done reading lists!!!!!!!!!!!!!!!!!!!!!\n")

more_loaded_things = {}
with open("dict.txt", "r") as file_in:
    for item in file_in:
        key, value = item.rstrip("\n").split(":")
        more_loaded_things[key] = value
print(dumps(more_loaded_things, indent=indent_char))

city_locations = {}
with open("city_locations.txt", "r") as file_in:
    for item in file_in:
        city, lon, lat = item.rstrip("\n").split(":")
        more_loaded_things[city] = (lon, lat)
print(dumps(more_loaded_things, indent=indent_char))

with open("tuple_things.txt", "r") as file_in:
    tuple_things = tuple(file_in.read().strip("(").strip(")").rstrip("\n").split(", "))
    print(tuple_things)

with open("mixed_tuple.txt", "r") as file_in:
    loaded_tuple = ast.literal_eval(file_in.read())
    print(loaded_tuple)

# yes i was lazy with this :P
with open("things_set.txt", "r") as file_in:
    loaded_map = ast.literal_eval(file_in.read())
    print(loaded_map)