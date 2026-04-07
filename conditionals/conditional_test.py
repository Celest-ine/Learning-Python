# Use user input to test a series of conditions and print a message based on the results.
# Get user input
name = input("What is your name? ").lower()
age = input('How old are you? ')

if not name:
    print('You did not enter a name.')
elif not age.isdigit():
    print('Enter a valid age.')
elif age < 18:
    print(f'{name.title()}, you are still a minor.')
    print('You cannot vote yet.')
elif age == 18:
    print(f'{name.title()}, congratulations on reaching adulthood!')
    print('Go register as a voter.You can now vote!')
else:
    print(f'{name.title()}, you are an adult.')
    print('Hope you are a registered voter!')