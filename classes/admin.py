"""A class that represents an admin and the admins privileges."""
from users import User

class Privileges:
    """Describes the privileges fo special users."""

    def __init__(self, privileges=None):
        """Initialise the attribute of the class."""

        if privileges is None: # To avoid making default value mutable so that each object gets its own list
            privileges = [
                "can post",
                "can delete post",
                "can ban user"
                "can add user",
            ]

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