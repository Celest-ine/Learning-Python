def describe_city(city, country='kenya'):
    """Print a simple sentence about a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city("nairobi")
describe_city("mombasa")
describe_city("abuja", "nigeria")