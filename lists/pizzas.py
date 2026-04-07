# A list that uses a for loop to print  a sentence for each item in the list.
pizzas = ['beef barbeque', 'diavola', 'hawaiian', 'pepperoni', 'margherita']

# Use slice to print the first three items in the list.
print('The first three items in the list are:')
for pizza in pizzas[:3]:
    print(f'{pizza.title()} pizza')

# Use slice to print two items from the middle of the list.
print('\nTwo items from the middle of the list are:')
for pizza in pizzas[3:5]:
    print(f'{pizza.title()} pizza')

# use slice to print the last three items in the list.
print('\nThe 3 last items in the list are:')
for pizza in pizzas[-3:]:
    print(f'{pizza.title()} pizza')

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

# A sentence at the end of the for loop, outside the for loop.
favorite_pizza = pizzas[0]
print(f"\nMy favorite pizza of them all is {favorite_pizza} pizza.\nPizza makes me happy!\nI really love pizza!")