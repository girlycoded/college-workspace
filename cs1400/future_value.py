# name: joosan
# desc: calculate the future of a monthly deposit given a monthly deposit amount , the interest rate, and th enumber of deposits

monthly_deposit_amount = 0.0
interest_rate = 0
month_count = 0
future_value = 0.0

print("Interest calculator ---")
monthly_deposit_amount = float(input("Enter the deposit amount: "))
interest_rate = float(input("Enter the interest rate: "))
month_count = int(input("How many months will this be deposited for? "))

monthly_rate = interest_rate / 100 / 12

for count in range(month_count):
    future_value = (future_value + monthly_deposit_amount) * (1 + monthly_rate)


print(f"If you deposit ${monthly_deposit_amount:.2f} a month for {month_count} months at {interest_rate:.1f}% interest, you will end up with ${future_value:.2f}")