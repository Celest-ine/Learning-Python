# A loop that allows users to enter as many toppings until they are finished.

prompt = "Enter a pizza topping that you would like:"
prompt += "\n(Enter 'quit' when you are finished.)"

# Modify the code to store the inputs in a list and print all the toppings enterted.
toppings = []
while True:
    pizza_topping = input(prompt)
    
    if pizza_topping.lower() == "quit":
        print("Finished adding pizza toppings.")
        break
    toppings.append(pizza_topping)
    print(f"You have added {pizza_topping} to your pizza.")

print(f"Here are your {len(toppings)} toppings: ")
for topping in toppings:
    print(f"- {topping}")