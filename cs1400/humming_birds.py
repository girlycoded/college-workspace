# name: joosan tibbetts
# desc: practice IF structure while learning about humming birds

name = (input("What is the name of your humming bird? ") or "").lower()

if name == "speedy" or name == "gonzales":
    print("That's not a very original name!")
elif name == "chick":
    print("That's what baby humming birds are called!")
elif name == "beep beep":
    print("wait... beep beep is a roadrunner!")
else:
    print(name, "is a beautiful name.")

heart_rate = int(input(f"how fast does {name}'s heart beat? "))
if heart_rate > 20 and heart_rate < 60:
    print("You must be doing yoga")
elif heart_rate is 60:
    print("That is very specific")
elif 60 < heart_rate < 100:
    print("Watching TV?")
elif heart_rate >= 100:
    print(f"{heart_rate} beats per minute is still not as fast as {name}'s heart rate. ")
    print(f"{name}'s heart beats at 1200 BPM and he takes approximately 250 breaths per minute. ")
else:
    print("u alive?")

# wings beat speed
speed = float(input(f"im like hey whats up hello. How fast do {name}'s wings beat? "))
weight = float(input(f"How much does {name} weigh?"))
print("\n" * 3)

if speed > 150 and heart_rate > 199:
    print("you'll never catch em")
elif name == "speedy":
    name = input("enter a new bird name: ").lower()
    if name == "big bird":
        print("thats much worse. IM THE BIGGEST BIRD IM THE BIGGEST BIRD")
    else:
        print("okay new name")