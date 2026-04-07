# A tuple of foods a buffet-style restaurant offers.
buffet = ('sushi', 'mushroom soup', 'T-bone steak', 'mashed potatoes', 'chocolate mousse')
for food in buffet:
    print(food)
print()

# Try to change one of the items. This will cause an error because tuples are immutable.
#buffet[1] = 'clam chowder'

#Rewrite the tuple to replace some foods. The only way to change a tuple.
buffet = ('sushi', 'clam chowder', 'T-bone steak', 'baked potatoes', 'chocolate mousse')
for food in buffet:
    print(food)