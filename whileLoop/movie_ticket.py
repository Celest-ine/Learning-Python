# A loop asks the user for their age and determines the ticket price.

prompt = "Please enter your age: "
prompt += "\n(Enter 'quit' to exit)"

while True:
    age = input(prompt)

    if age.lower() == 'quit':
        break
    elif age.strip() == "":
        print("Please enter a valid age.")
        continue
    elif not age.isdigit():
        print("Please enter a numeric age.")
        continue

    age = int(age)
    if age < 3:
        print("The ticket is Free.")
    elif age < 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")