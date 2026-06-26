def make_sandwich(*items):
    """Accept a list of items that a user wants in their sandwich."""
    print("Your sandwich will have the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("peanut butter", "jam")
print()
make_sandwich("avocado")
print()
make_sandwich("ham", "tomatoes", "onions", "mayonaise")