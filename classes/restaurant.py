class Restaurant:
    """Simulates an instance of a resturant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initiate restutant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the description of the resturant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Prints a message indicating that the resturant is open."""
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Sarovar", "Italian")
restaurant_1 = Restaurant("Biriyani House", "Indian")
restaurant_2 = Restaurant("Java cafe", "Continental")
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant.describe_restaurant()
restaurant.open_restaurant()