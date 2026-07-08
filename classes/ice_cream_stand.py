"""Ice cream stand class that inherits properties of Restaurant."""

from number_served import Restaurant


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