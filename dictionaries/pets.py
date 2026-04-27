# Dictionaries of pets
dog = {
    "name": "chase",
    "type": "dog",
    "owner": "liz",
    "colour": "black",
    "breed": "chowchow",
}
cat = {
    "name": "sky",
    "type": "cat",
    "owner": "john",
    "colour": "grey",
    "breed": "ragdoll",
}
gold_fish = {
    "name": "nemo",
    "type": "fish",
    "owner": "andy",
    "colour": "orange",
    "breed": "goldfish",
}

pets = [dog, cat, gold_fish]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['type']} owned by {pet['owner'].title()}.")
    print(f"It's a {pet['breed']} breed.")
    print()