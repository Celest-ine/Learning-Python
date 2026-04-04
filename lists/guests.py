# A list of invited guests and invitation message

guests = ['Paul', 'Joy', 'Blue', 'Victor']
print(len(guests))
# Modify to use for loop to print the invitation
for guest in guests:
    print(f'\nDear {guest}, you are invited to my dinner party this Saturday.')

# remove the guest that can't make it and replace them with a new person
cannot_make_it = guests[2]
guests.remove(cannot_make_it)

print(f'{cannot_make_it} cannot make it for the dinner')
guests.insert(2, 'Cate')
print(guests)

for guest in guests:
    print(f'\nDear {guest}, you are invited to my dinner party this Saturday.')

print('\nI found new people who would like to attend the dinner.')

# Add new guests to the list using the append() and insert() methods
guests.insert(0, 'Ivy')
guests.insert(2, 'John')
guests.append('Mark')

for guest in guests:
    print(f'\nDear {guest}, you are invited to my dinner party this Saturday.')
print(guests)

print('There has been a problem with the organisation of this dinner.\nI can only invite two guests')

# Use pop() to remove guests from the list
popped_guest = guests.pop()
print(f'Dear {popped_guest}, Sorry but we have to cancel the dinner invite')
popped_guest = guests.pop()
print(f'Dear {popped_guest}, Sorry but we have to cancel the dinner invite')
popped_guest = guests.pop()
print(f'Dear {popped_guest}, Sorry but we have to cancel the dinner invite')
popped_guest = guests.pop()
print(f'Dear {popped_guest}, Sorry but we have to cancel the dinner invite')
popped_guest = guests.pop()
print(f'Dear {popped_guest}, Sorry but we have to cancel the dinner invite')
print(guests)

print(f'Dear {guests[0]}, you are still invited for the dinner')
print(f'Dear {guests[1]}, you are still invited for the dinner')

# Use del to remove list items
del guests[1]
print(guests)
del guests[0]
print(guests)