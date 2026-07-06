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
        """Sets the number of customes served"""
        
        self. number_served = number_served

    def open_restaurant(self):
        """Prints a message indicating that the resturant is open."""
        
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Sarovar", "Italian")

restaurant_1 = Restaurant("Biriyani House", "Indian")

restaurant_2 = Restaurant("Java cafe", "Continental")

restaurant_1.set_number_served(50) # setting the number of customers served using a method
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print()

restaurant_2.number_served = 120 # accesing the attribute directly
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
print()

restaurant.set_number_served(200)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()