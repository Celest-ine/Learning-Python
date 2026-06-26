def make_sandwich(*items):
    """Accept a list of items that a user wants in their sandwich."""
    print("Your sandwich will have the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("peanut butter", "jam")
make_sandwich("avocado")
make_sandwich("ham", "tomatoes", "onions", "mayonaise")