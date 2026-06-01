# name: joosan tibbetts
# desc: for loops

for index in range(5, 10):
    print("index", index)

for index in range(12):
    print("I have", index + 1, "cookies")

age = 5

for count in range(age):
    print(count + 1, f"birthday greeting{"" if age == 1 else "s"}")

print("\n" * 2)

for i in range(0, 11, 5):
    print(i)

print()

for i in range(10, 0, -1):
    print(i)

cookies = int(input("How many cookies do you have? "))
for cookie_count in range(cookies, 0, -1):
    if cookie_count > 1:
        print(f"I have {cookie_count} cookies!")
    else:
        print("I have one cookie left MWAHAHAHAHA")

for cookie_count in range(cookies, 0, -1):
    print(f"{cookie_count} cookies!" if cookie_count > 1 else "You have one cookie left! MWAHAHAHAHAHA")
