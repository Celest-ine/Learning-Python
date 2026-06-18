# List of sandwitch orders

sandwitch_orders = ['chicken', 'pastrami','grilled cheese','pastrami', 'avocado', 'reuben', 'pastrami','cuban', 'italian panini']
finished_sandwitches = []

print("Sorry, we are out of pastrami today.")

#Loop to remove all instances of 'pastrami' from the sandwitch orders.
while 'pastrami' in sandwitch_orders:
    sandwitch_orders.remove('pastrami')
    
# Loop through the sandwitch orders and print a message for each order.
while sandwitch_orders:
    sandwitch = sandwitch_orders.pop()
    print(f"I made your {sandwitch} sandwitch.")
    finished_sandwitches.append(sandwitch)

# Print a message for each finished sandwitch.
print("\nThe following sandwitches have been made:")
for made_sandwich in finished_sandwitches:
    print(f"- {made_sandwich}")