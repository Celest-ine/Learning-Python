"""A class that prints the side of a die rolled."""

from random import randint

class Die:
    """Represent an aspect of a die."""

    def __init__(self, sides=6):
        """Instatiate the attributes of die"""

        self.sides = sides
    
    def roll_die(self):
        """Print a random number between 1 and the number of sides a die has."""
        
        face_of_die = randint(1, self.sides)
        print(f"Your rolled a {face_of_die}")

my_die_roll = Die()
my_die_roll.roll_die()

ben_die_roll = Die(20)
ben_die_roll.roll_die()

sarah_die_roll = Die(10)
sarah_die_roll.roll_die()