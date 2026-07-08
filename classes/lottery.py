from random import choices

class Lottery:
    """A class that randomly selects 4 numbers out of 10 or letters out of 5 to be the winning ticket."""

    def __init__(self, numbers=(8, 4, 7, 6, 1, 3, 9, 15, 17, 42,), characters=('r', 'h', 'v', 'a', 'j')):
        """Instantiate the attributes of the class."""

        self.numbers = numbers
        self.characters = characters

    def display_ticket(self):
        """Displays the winning ticket."""

        batch = choices(self.numbers, self.characters)
        ticket = []

        if batch == self.numbers:
            for _ in range(4):
                number = choices(self.numbers)
                ticket = number.append()

        else:
            for _ in range(4):
                char = choices(self.characters)
                ticket = char.append()

        print(f"The winning ticket is {ticket}")

bas_lottery = Lottery()
bas_lottery.display_ticket()