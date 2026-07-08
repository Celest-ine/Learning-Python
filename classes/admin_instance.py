"""Create an instance of Admin."""
from users import User, Privileges, Admin

joy = Admin("Joy", "Ndanu", 30, "Kenya", "Ai Engineer")
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