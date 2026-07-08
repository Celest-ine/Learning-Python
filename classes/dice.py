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

six_die_roll = Die()
for _ in range(10):
    six_die_roll.roll_die()

twenty_die_roll = Die(20)
twenty_die_roll.roll_die()

ten_die_roll = Die(10)
ten_die_roll.roll_die()