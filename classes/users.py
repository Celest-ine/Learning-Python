class User:
    """Simulate a user profile."""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize first name, last name, age, location, and occupation attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"User Profile:\nName: {self.first_name} {self.last_name} \nAge: {self.age} \nLocation: {self.location} \nOccupation: {self.occupation}")

    def increment_login_attempts(self):
        """Increments the number of login attempts by 1."""
        self.login_atempts += 1

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}. Welcome to our platform!")

jane = User("Jane", "Doe", 28, "New York", "Software Engineer")
mary = User("Mary", "Bling", 49, "Uganda", "Data Scientist")
jack = User("Jack", "Sparrow", 35, "Caribbean", "Pirate")

jane.describe_user()
jane.increment_login_attempts()
jane.increment_login_attempts()
jane.increment_login_attempts()
jane.greet_user()
print()

mary.describe_user()
mary.greet_user()
print()

jack.describe_user()
jack.greet_user()