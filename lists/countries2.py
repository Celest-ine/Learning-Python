# Use user input to create a list of countries. Then, print the list.

countries = input('Enter a list of countries, separeted by spaces:').lower()
countries_list = countries.split()
if not countries_list:
    print('No countries were entered.')
else:
    for country in countries_list:
        print(f'-{country}')

# Add a country to the list and print it
add_country = input('Enter a country to add to the list: ').lower()
countries_list.append(add_country)
for country in countries_list:
    print(f'-{country}')

# Remove a country from the list
remove_country = input('Enter a country to remove from the list: ').lower()
if remove_country in countries_list:
    countries_list.remove(remove_country)
else:
    print(f'{remove_country} is  not in the list.')
for country in countries_list:
    print(f'-{country}')

# Sort the list of counries and print it
countries_list.sort()
print('These are the countries in alphabetical order:')
for country in countries_list:
    print(f'-{country}')