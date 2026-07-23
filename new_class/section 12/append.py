# name: joosan
# desc: append file

import os, time

this_directory = os.path.dirname(__file__)
file_out_path = f"{this_directory}/my_append.txt"

with open(file_out_path, "a") as file_out:
    text = ""
    while text.lower() != 'd':
        # time.sleep(2)
        file_out.write(f"{text}\n")
        text = input("enter stuff to write: ")
