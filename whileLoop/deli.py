# List of sandwich orders

sandwich_orders = ['chicken', 'grilled cheese', 'avocado', 'reuben', 'cuban', 'italian panini']
finished_sandwiches = []

# Loop through the sandwich orders and print a message for each order.
while sandwich_orders:
    current_order = sandwich_orders.pop(0) # So that the list of the orders does not change.
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print a message for each finished sandwich.
print("\nThe following sandwiches have been made:")
for made_sandwich in finished_sandwiches:
    print(f"- {made_sandwich}")