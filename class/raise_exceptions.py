#name: joosan
#desc: raise exceptions

user_input = input("How old are you? ")
try:
    age = int(user_input)
    if age < 0: raise ValueError("Age cannot fall below zero!")
except BaseException as e:
    print(e) 

# specific exception
while True:
    name = input("What is your name (don't say bob): ").lower()
    try:
        if name == "bob": raise NameError("F*ck you bob. Try again.")
        elif not name.isalpha(): raise NameError("NO NON-ALPHA CHARACTERS DIE DIE DIE")
        break
    except NameError as e:
        print(f"Invalid input: {e}")