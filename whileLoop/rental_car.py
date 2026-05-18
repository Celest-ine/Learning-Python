# A program that asks the user what kind of rental car they would like and prints amessage about the car.
car = input("What kind of car would you like to rent? ").strip()

if not car:
    print("You need to enter a car model.")
else:
    print(f"Let me see if I can find you a {car.title()}.")