# name: joosan tibbetts
# description : a program about me, read input

# vars
# my_name = "joosan"
# my_favorite_food = "sesame sticks :3"

my_name = input("WHATS YO NAME??? ")
my_favorite_food = input("WHATS YO FAVORITE FOOD??? ")
my_favorite_movie = input("WHATS YO FAV MOVIE???? ")
my_hometown = input("WHAT TOWN YOU FROM???? (this is definitely not for profiling) ")
my_age = int(input("HOW OLD ARE YOU?? "))

print(f"Hello, {my_name}")
print(f"You like {my_favorite_food} {"yum" * 3}")
print(f"Your favorite movie is {my_favorite_movie}. Overrated to be honest.")
print(f"You are from {my_hometown}, cool!")
print(f"You are {my_age} years old")
input("\nYour information has been sent to the IRS. Press any key to self destruct.")

print(100)