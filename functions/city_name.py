def city_country(city, country):
 """A function that returns a city, country pair."""
 formatted_string = f"{city}, {country}"
 return formatted_string.title()

nairobi_location = city_country('nairobi', 'kenya')
kampala_location = city_country('kampala', 'uganda')
abuja_location = city_country('abuja', 'nigeria')

print(nairobi_location)
print(kampala_location)
print(abuja_location)