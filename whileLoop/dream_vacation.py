# A program that polls the user about their dream vacation and prints the results.

poll = {}

poll_active = True
while poll_active:
    name = input("\nWhat is your name? ")
    response = input("\nIf you could visit a place in the world, where would you go? ")
    poll[name] = response

    # Ask if anyone else wants to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat.lower().strip() in ['no', 'n', 'nope']:
        poll_active = False

# Print poll results.
print("\n--- Poll Results ---")
for name, response in poll.items():
    print(f"{name.title()} would like to visit {response.title()}.")