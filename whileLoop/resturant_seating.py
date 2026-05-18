""" A program that asks the user how many people are in their dinner group.
If the answer is more than eight, Print a message saying they'll have to wait for a table.
"""

# Get the number of people in the dinner group
prompt = input("How many people are in your dinner group? ")

if prompt.isdigit():
    dinner_group_size = int(prompt)

# Check if the dinner group size is more than 8
    if dinner_group_size > 8:
        print("You'll have to wait for a table.")
    else:
        print("Your table is ready.")
else:
    print("Please enter a number instead.")