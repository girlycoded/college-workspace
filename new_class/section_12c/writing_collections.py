#name: joosan
#desc: write collections to file

things = ["laptop", "coffee", "book", "keys"]

with open("things.txt", "w") as file_out:
    for item in things:
        file_out.write(f"{item}\n")

with open("things_in_line.txt", "w") as file_out:
    file_out.write(", ".join(things))

print("Writing list completed!")