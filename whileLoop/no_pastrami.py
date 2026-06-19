# List of sandwich orders

sandwich_orders = ['chicken', 'pastrami','grilled cheese','pastrami', 'avocado', 'reuben', 'pastrami','cuban', 'italian panini']
finished_sandwiches = []

print("Sorry, we are out of pastrami today.")

#Loop to remove all instances of 'pastrami' from the sandwich orders.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
# Loop through the sandwich orders and print a message for each order.
while sandwich_orders:
    current_order = sandwich_orders.pop(0) # So that the list order does not change.
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print a message for each finished sandwich.
print("\nThe following sandwiches have been made:")
for made_sandwich in finished_sandwiches:
    print(f"- {made_sandwich}")