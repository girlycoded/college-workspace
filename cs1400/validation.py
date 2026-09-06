choice = 0

while True:
    choice = int(input("1. Add Customer\n2. View customer\n3. Exit Enter choice: "))

    if (choice == 1 or choice == 2 or choice == 3): break

    print("Invalid selection")

# sentinel controled loop
total_sales = 0.0
sales = float(input("Enter sale amount (0 to quit): "))

while sales != 0:
    total_sales += sales
    sales = float(input("Enter another sale amount (0 to quit): "))

print(f"Total sales: {total_sales:.2f}")