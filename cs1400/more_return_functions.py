# name: joosan tibbetts
# desc: more functions

# CONSTS
OVERTIME_MARGIN = 40
OVERTIME_RATE = 0.5

# FUNCS
def from_seconds(seconds: float):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    return f"{hours} hours, {minutes} minutes, {remaining_seconds} seconds"

def is_valid_password(password: str):
    return len(password) > 7 and not password.isalpha()


def paycheck(hours: float, rate: float):
    overtime_pay = 0
    if hours > OVERTIME_MARGIN:
        overtime_pay += (hours - OVERTIME_MARGIN) * rate * OVERTIME_RATE

    return hours * rate + overtime_pay

# MAIN
print(f"Weekly pay: ${paycheck(41, 199):,.2f}")
password_valid = is_valid_password(input("Enter a password"))

print("Password accepted" if password_valid else "Password denied")
print(from_seconds(float(input("How many seconds"))))