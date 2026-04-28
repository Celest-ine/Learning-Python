# A dictionary that maps names to their favorite numbers.
# Modify for each person to have more than one number.
favorite_numbers = {
    "joy": [6, 8, 9],
    "ivy": [9, 4, 2],
    "bahati": [3, 1, 4, 5, 8],
    "kim": [7, 2],
    "alex": [4, 6, 3, 7],
}
# Print each person's name and their favorite number.
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")