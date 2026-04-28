# A dictionary with a dictionary as its value.
cities = {
    "nairobi": {
        "country": "Kenya",
        "approximate_population": 5_700_000,
        "fact": "It is the only capital city in the world to host a national pack within its boundaries",
    },

    "paris": {
        "country": "France",
        "approximate_population": 2_040_000,
        "fact": "It was originally named Lutetia",
    },
    "london": {
        "country": "England, United Kingdom",
        "approximate_population": 9_100_000,
        "fact": "It is the capital city for both England and United Kingdom",
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    for key, value in city_info.items():
        print(f"\t{key.replace('_', ' ').title()} - {value}")