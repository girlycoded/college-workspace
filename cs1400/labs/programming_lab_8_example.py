dogs = []

def add_dog():
    new_dog_name = input("What is the name of your dog? ")
    dog_days_staying = input("How many days is your dog staying? ")

    new_dog = {
        "name": new_dog_name,
        "days_staying": dog_days_staying,
    }
    dogs.append(new_dog)

add_dog()
add_dog()

dog_to_search_for = input("What dog would you like to search for? ").upp().strip()

for dog in dogs:
    if dog["name"] == dog_to_search_for:
        print(dog["days_staying"])
        break

# print(dogs)