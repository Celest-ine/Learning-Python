# An if-elif-else chain to determine a persons stsge of life.
age = input("Enter your age: ")

if not age.isdigit():
    print("Enter a valid age.")
else:
    age = int(age)

    if age < 2:
        print("You are a baby.")
    elif age < 4:
        print("You are a toddler.")
    elif age < 13:
        print("You are a kid.")
    elif age < 20:
        print("You are a teenager.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are an elder.")