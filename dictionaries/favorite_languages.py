# A dictionary of people and their favorite languages.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# A list of people who should take the favorite languages poll.
poll_requests = ['mary', 'jen', 'joy', 'brian', 'sarah', 'kim']

# Print a message thanking those who took the poll and inviting those who haven't taken.
for name in poll_requests:
    if name in favorite_languages.keys():
        print(f'Thank you, {name.title()}, for taking the poll.')
    else:
        print(f'{name.title()}, please take our poll!')