#name: joosan
#desc: learn about sets

classes = {"CS1400", "ANTH1020", "MATH1060", "MATH1060", "MATH1220", "ENGL1010"}
print(classes)

classes.add("JPNS1020")
print(classes)

classes.remove("CS1400")
classes.discard("MATH1060")
print(classes)

print(len(classes))

print("found" if "CS1400" in classes else "not found")

for class_name in classes:
    print(class_name)

print(sorted(classes))

names = ("Samy", "Davis", "Junior", "Neil", "Patrick", "Harris", "Eli", "Manning", "Samy")
for name in names:
    if len(name) > 5:
        print(name)

my_name = input("Enter your bane: ").split()
print(my_name, tuple(my_name), set(my_name))