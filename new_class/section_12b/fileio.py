# name: joosan
# desc: read file

file_name = "my_read.txt"

# try: # ugly nesting
#     with open(file_name, "a") as file_out:
#         while True:
#             text = input("Enter a line of text to the file (Enter to quit): ")
#             if not text: break

#             file_out.write(f"{text}\n")
#             print("Writing to file")
# except OSError as e: print(f"File system error occured {e}")

# # open the file to read

try:
    with open(file_name, "r") as file_in:
        print("Where is the pointer?", file_in.tell())
        content = file_in.readline()
        print(content, file_in.tell())

        file_in.seek(0)
        print(file_in.tell())

        for line in file_in:
            input_text = line.split()
            print(input_text)
            if len(input_text) < 2: print("Invalid formatting"); continue

            first = input_text[0]
            second = input_text[1]
            print(second, first)
            
except Exception as e: print(f"File system error occured {e}")