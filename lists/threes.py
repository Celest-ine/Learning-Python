# A list of the multiples of 3 between 1 and 30 inclusive.
threes = []
for number in range(1, 31):
    if number % 3 == 0:
        threes.append(number)
print(threes)