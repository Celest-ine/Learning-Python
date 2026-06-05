# Ask the user for a number and report whether the number is a multiple of ten.

number = int(input("Enter a number and I will tell you if it's a multiple of 10, 5 only, or none of them: "))

# Modify the code to check if a number is a multiple of 10 and 5, one of them or none of them.
if number % 10 == 0:
    print(f"{number} is a multiple of both 10 and 5.")
elif number % 5 == 0:
    print(f"{number} is a multiple of 5 but not 10.")
else:
    print(f"{number} is neither a multiple of 10 nor 5.")