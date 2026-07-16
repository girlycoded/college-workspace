import bank

balance = 500

amount = float(input("How much would you like to deposit? "))
balance = bank.deposit(balance, amount)
print("new balance:", balance)

amount = float(input("How much would you like to deposit? "))
balance = bank.withdraw(balance, amount)
print("new balance:", balance)