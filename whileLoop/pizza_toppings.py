# A loop that allows users to enter as many toppings until they are finished.

prompt = "Enter a pizza topping that you would like:"
prompt += "\n(Enter 'quit' when you are finished.)"

# Modify the code to store the inputs in a list and print all the toppings enterted.
toppings = []
while True:
    pizza_topping = input(prompt)
    
    if pizza_topping.lower() == "quit":
        print("\nFinished adding pizza toppings.")
        break
    elif pizza_topping.strip() == "":
        print("\nYou did not enter a topping. Please try again.")
        continue
    toppings.append(pizza_topping)
    print(f"\nYou have added {pizza_topping} to your pizza.")

if len(toppings) == 0:
    print("\nYou did not add any toppings to your pizza.")
else:
    print(f"\nHere are your {len(toppings)} toppings: ")
    for topping in toppings:
        print(f"- {topping}")