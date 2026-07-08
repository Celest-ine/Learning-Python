# Use the resturant class to add a attribute, number_served, with a default value of 0.
class Restaurant:
    """Simulates an instance of a resturant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initiate restutant name and cuisine type attributes."""
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the description of the resturant."""
        
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
        print(f"{self.restaurant_name} has served {self.number_served} customers.")

    def set_number_served(self, number_served):
        """Sets the number of customers served"""
        
        if number_served >= 0:
            self.number_served = number_served
        else:
            print("Number of customers served cannot be negative.")

    def increment_number_served(self, additional_customers):
        """Increments the number of customers served."""
        
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("Additional customers cannot be negative.")

    def open_restaurant(self):
        """Prints a message indicating that the resturant is open."""
        
        print(f"{self.restaurant_name} is now open!")