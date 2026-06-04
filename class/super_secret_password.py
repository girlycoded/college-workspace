# name: joosan tibbetts
# desc: supersecret password

#force a valid password within 3 tries
MAX_ATTEMPTS = 3
PASSWORD = "bob"

attempts = 1

logged_in = False

while attempts <= MAX_ATTEMPTS:
    user_input = input("What is the password? ")
    if user_input == PASSWORD:
        logged_in = True
        break
    else:
        print(f"Wrong password. You have {MAX_ATTEMPTS - attempts} attempt(s) left.")
    
    attempts += 1

if logged_in:
    print("Password accepted! Thankyou!")
else:
    exit()

# rest of program