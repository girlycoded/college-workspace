# compare loops

count = 0
while count < 10:
    print(count)
    count += 1

# for loop
for i in range(10):
    print(i)

# while loop is more **robust**
# does not have to count

again = "y"
while again.lower().startswith("y"):
    print("this is fun!!!")
    again = input("Do you want to do this again? (y/n) ")

print("\n")