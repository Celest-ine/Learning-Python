# A tuple of foods a buffet-style resturant offers.
buffet = ('sushi', 'mashroom soup', 'T-bone steak', 'mushed potatoes', 'chocolate mousse')
for food in buffet:
    print(food)
print('\n')
# Try to change one of the items. This will cause an error because tuples are immutable.
#buffet[1] = 'clam chowder'

#Rewrite the tuple to replce some foods. The only way to change a tuple.
buffet =('sushi', 'clam chowder', 'T-bone steak', 'baked potatoes', 'chocolate mousse')
for food in buffet:
    print(food)