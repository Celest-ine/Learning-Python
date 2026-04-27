# A dictionary with information about a person
# Modify the code to have three dictionaries and store all three dictionaries in a list.
person1 = {
    "first_name": "celeste",
    "last_name": "wangechi",
    "age": 25,
    "city": "nairobi",
}
person2 = {
    "first_name": "blue",
    "last_name": "ren",
    "age": 20,
    "city": "paris",
}

person3 = {
    "first_name": "paula",
    "last_name": "green",
    "age": 23,
    "city": "florida"
}
people = [person1, person2, person3]

# Loop through the list and print info about each person.
for person in people:
    print(f"Fullname: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city'].title()}")
    print()