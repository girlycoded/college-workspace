# name: joosan
# desc: secret file

# CONSTS
import os, getpass
BOLD = "\033[1m"; IL = "\033[3m"; UL = "\x1b[4m"; UB = "\033[22m"; YELLOW = "\033[33m"; BLUE="\033[34m"; RESET = "\033[0m"; CLR = "\033c";

# VARS
this_directory = os.path.dirname(__file__)
file_out_path = f"{this_directory}/super_secret_file.txt"

name = getpass.getuser()
print(f"{CLR}Your spy name is {BLUE}{name}{RESET}")

while True:
    password = getpass.getpass("Enter the secret password: ")
    if password == "": break

    print(f"{YELLOW}Wrong password. Every. Secret. Deleted{RESET}")
    with open(file_out_path, "w") as file_out: file_out.write("")

while True:
    with open(file_out_path, "a") as file_out:
        secret_text = input("Enter stuff to write to the super secret file (q to quit): ")
        if secret_text.lower() == "q": break

        file_out.write(f"{name}: {secret_text}\n")

print("Have a great spy day", name)