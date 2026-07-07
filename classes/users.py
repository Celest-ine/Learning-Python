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
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Resets the number of login attemts back to 0."""
        self.login_attempts = 0

    def display_login_attempts(self):
        """Displays the number of login attempts."""
        print(f"Login attempts: {self.login_attempts}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}. Welcome to our platform!")


class Privileges:
    """Describes the privileges fo special users."""

    def __init__(self, privileges=["can post", "can delete post", "can ban user", "can add user"]):
        """Initialise the attribute of the class."""

        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges of the admin user."""

        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Represent an admin user."""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an admin user.
        """
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = Privileges()
    
joy = Admin("Joy", "Ndanu", 30, "Kenya", "Ai Engineer")
jane = User("Jane", "Doe", 28, "New York", "Software Engineer")
mary = User("Mary", "Bling", 49, "Uganda", "Data Scientist")
jack = User("Jack", "Sparrow", 35, "Caribbean", "Pirate")

joy.describe_user()
joy.privileges.show_privileges()
joy.increment_login_attempts()
joy.increment_login_attempts()
joy.increment_login_attempts()
joy.increment_login_attempts()
joy.display_login_attempts()
joy.reset_login_attempts()
joy.display_login_attempts()
print()

jane.describe_user()
jane.increment_login_attempts()
jane.increment_login_attempts()
jane.increment_login_attempts()
jane.display_login_attempts()
jane.reset_login_attempts()
jane.display_login_attempts()
jane.greet_user()
print()

mary.describe_user()
mary.greet_user()
print()

jack.describe_user()
jack.greet_user()