# A list of invited guests and invitation message

guests = ['Paul', 'Joy', 'Blue', 'Victor']
message = 'You are invited for dinner at my house.'

print(guests)

print(f'Dear {guests[0]},  {message}')
print(f'Dear {guests[1]},  {message}')
print(f'Dear {guests[2]},  {message}')
print(f'Dear {guests[3]},  {message}')

# remove the guest that can't make it and replace them with a new person
cannot_make_it = 'Blue'
guests.remove(cannot_make_it)

print(f'{cannot_make_it} cannot make it for the dinner')
guests.insert(2, 'Cate')
print(guests)

print(f'Dear {guests[0]},  {message}')
print(f'Dear {guests[1]},  {message}')
print(f'Dear {guests[2]},  {message}')
print(f'Dear {guests[3]},  {message}')

print('\nI found new people who would like to attend the dinner.')

# Add new guests to the list using the append() and insert() methods
guests.insert(0, 'Ivy')
guests.insert(2, 'John')
guests.append('Mark')

print(f'Dear {guests[0]},  {message}')
print(f'Dear {guests[1]},  {message}')
print(f'Dear {guests[2]},  {message}')
print(f'Dear {guests[3]},  {message}')
print(f'Dear {guests[4]},  {message}')
print(f'Dear {guests[5]},  {message}')
print(f'Dear {guests[6]},  {message}')
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