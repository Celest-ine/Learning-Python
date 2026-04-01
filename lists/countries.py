# Use list methods to add, remove, and sort a list of countries.

countries = ['kenya', 'uganda', 'tanzania', 'rwanda', 'burundi']
print('Original list of countries:', countries)

# Add a country at the end of the list
countries.append('ethiopia')
print('After appending:', countries)

# Insert a country at a specific position
countries.insert(3, 'somalia')
print('After insertng at index 3:', countries)

# Remove a country at a specific position
del countries[2]
print('After deleting index 2:', countries)

# Remove a country from the end of the list
popped_country = countries.pop()
print('Popped country:', popped_country)
print('After popping the last country:', countries)

# remove a country by value
removed_country = 'rwanda'
if removed_country in countries:
    countries.remove(removed_country)
print('Removed country:', removed_country)
print('After removing by value:', countries)

# Temporary sort a list
print('Temporarily sorted list:', sorted(countries))
print('List after temporary sort:', countries)

# Reverse the list
countries.reverse()
print('Reversed list:', countries)

# Permanently sort the list
countries.sort()
print('Permanently sorted list:', countries)

# sort the list in reverse
countries.sort(reverse=True)
print('Permanently sorted in reverse:' , countries)
