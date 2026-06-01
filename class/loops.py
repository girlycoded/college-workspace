# name: joosan tibbetts
# desc: practice while loops

# the same thing over and over

count = 0
while count <= 5:
    print("I am inside a while loop!")
    count += 1

count = 20
while count >= 0:
    print(count)
    count -= 1

count = 1
while count <= 5:
    print(count)
    count += 1

count = 1
total = 0

while count <= 5:
    total += count # accumulation!
    count += 1
    print("accumulated total", total)

initial_count = 10
count = 10
total = 45.0
while count > 0:
    total -= 1.5
    count -= 1
    print(total)

# your turn
print("average accumulation", (total - (initial_count * 1.5)) / initial_count)
