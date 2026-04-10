# A dictionary of major rivers and the countries they flow through.
rivers = {
    'nile': ['egypt', 'uganda', 'south sudan', 'sudan'],
    'amazon': ['brazil', 'peru', 'colombia'],
    'yangtze': ['china'],
    'mississippi': ['united states'],
    'congo': ['dr congo', 'angola', 'congo'],
}


# Print all the rivers in the dictionary.
print('This is a list of some major rivers in the world:')
for river in rivers:
    print(f'- {river.title()} River')
# Print the countries that each river flows through.
for river, countries in rivers.items():
    if len(countries) == 1:
        print(f'\nThe {river.title()} River flows through 1 country:')
    else:
        print(f'\nThe {river.title()} River flows through {len(countries)} countries:')
    for country in sorted(countries):
        print(f'- {country.title()}')