# name: joosan tibbetts
# desc: writing to files (input and output)

import os

this_directory = os.path.dirname(__file__)
file_out_path = f"{this_directory}/abc"

# file_out = open(file_out_path, "w")
# output_text = input("Enter some text to write to the file: ")

# file_out.write(output_text)
# file_out.write("\n")
# file_out.write(output_text)

# file_out.close()

try: 
    with open(file_out_path, "w") as file_out:
        file_out.write("hello world!")
except OSError as e:
    print(f"File system error occured: {e}")