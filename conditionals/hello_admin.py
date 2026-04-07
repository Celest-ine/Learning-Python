# Check if a user is an admin and greet them accordingly.

# users = ['admin', 'john', 'joy', 'sarah', 'james']
users = []
if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again.')
else:
    print('We need to find some users!')