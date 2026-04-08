# A dictionary that maps names to their favorite numbers.
favorite_numbers = {
    "joy": 6,
    "ivy": 9,
    "bahati": 3,
    "kim": 7,
    "alex": 4,
}
# Print each person's name and their favorite number.
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")