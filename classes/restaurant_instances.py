"""Create instances of Rstaurant and IceCreamStand."""

from number_served import Restaurant
from ice_cream_stand import IceCreamStand

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