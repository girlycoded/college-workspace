# name: joosan tibbetts
# desc: 

for number in range(1,11):
    if number == 6:
        print(f"Found the {number}!")
        break
    print(number)

for number in range(1, 11):
    if number == 5: continue
    print(number)

print("done")

for i in range(1, 21):
    if i % 2 == 0: continue
    print(i)

print("done with evens")
passcode = "ariana grande"

while True: #
    code = input("enter the secret code: ")

    if code == "ariana grande":
        print("access granted")
        break

    print("Incorrect super secret code. Try again!")

# ignore negative numbers
for index in range(5):
    number = int(input("Enter a number: ") or 0)

    if number < 0:
        print("negative numbers are ignored")
        continue

    print("You entered", number)

for index in range(1, 25):
    if index % 2 == 0: continue
    if index > 15: break

    print("Number is", index)

