# name: joosan
# desc: more filtering

import statistics

scores = [10, 20, 50, 55, 20, 99]

#count above average

count = 0
average = sum(scores) / len(scores)

for score in scores:
    if score > average:
        print(score)
        count += 1

print(f"Average: {average}\nCount: {count}")

print("Average (mean):", statistics.mean(scores))

students = ["Alice", "Bob", "Chris", "Dana"]
name = input("enter a name to search for: ").title().strip()

for index, student in enumerate(students):
    if student != name: continue
    print(f"Found student {name}")
    break
else:
    print(f"Could not find student {name}")

print("found" if name in students else "not found")