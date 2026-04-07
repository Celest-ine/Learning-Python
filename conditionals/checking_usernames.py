# A program that simulates how websites check that everyone has a unique user name.

current_users = ['blue', 'joy', 'Jason', 'mark', 'ruth']
#make a copy of current_users to make the check case insensitive
current_users_lower = [current_user.lower() for current_user in current_users]

new_users = ['james', 'jason', 'ivy', 'paul', 'joy']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Please enter a new user name, {new_user.title()} is already taken.')
    else:
        print(f'{new_user.title()} is available.')
