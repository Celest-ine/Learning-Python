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

class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant specific to an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        """Initialize attributes of the parent class.
         Then initialize attributes specific to an ice cream stand.
         """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def display_flavors(self):
        """Print the flavors available in the ice cream stand."""

        if self.flavors:
            print(f"{self.restaurant_name} offers the following flavors:")
            for flavor in self.flavors:
                print(f"- {flavor}")
        else:
            print(f"{self.restaurant_name} currently has no flavored ice cream available.")

my_ice_cream_stand = IceCreamStand("Sweet Treats")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.open_restaurant()
my_ice_cream_stand.flavors = ["blueberry", "vanilla", "chocolate fudge"]
my_ice_cream_stand.display_flavors()
print()

restaurant = Restaurant("Sarovar", "Italian")

restaurant_1 = Restaurant("Biriyani House", "Indian")

restaurant_2 = Restaurant("Java cafe", "Continental")

restaurant_1.set_number_served(50) # setting the number of customers served using a method
restaurant_1.increment_number_served(46)
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print()

restaurant_2.set_number_served(120) # setting the number of customers served using a method
restaurant_2.increment_number_served(70)
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
print()

restaurant.set_number_served(200)
restaurant.increment_number_served(38)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()