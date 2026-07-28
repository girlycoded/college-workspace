# name: joosan
# desc: grades

# name = ""
# wnum = ""
# gpa = 0.0
# age = 0
file_name = "Grade Report.txt"

try:
    with open(file_name, "a") as file_out:
        print("opening file...")        
        while True:
            name = input("Enter the student's last name (q to quit): ")
            if name == "q": break

            wnum = input("Enter their W-number: ")
            age = int(input("And their age: "))
            gpa = float(input("And their GPA: "))

            file_out.write(f"{name}, {wnum}, {age}, {gpa}\n")
            print("Writing to file...")
    print("Closing file...")
except OSError as e: print(f"File system error occured {e}")

try:
    with open(file_name, "r") as file_in:
        print("Opening file to read...")
        for student in file_in:
            text = student.split(", ")
            lname = text[0]
            lwnum = text[1]
            lage = text[2]
            lgpa = text[3]
            print(lname, lwnum, lage, lgpa)
    print("closing file")
except Exception as e: print(f"File system error occured {e}")