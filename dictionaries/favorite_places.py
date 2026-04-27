# A dictionary of peoples favorite places.
favorite_places = {
    "celeste": ["nairobi", "diani", "maasai mara"],
    "joy": ["naivasha", "paris", "detroit"],
    "joe": ["meru", "arusha", "vipingo"],
    "mark": ["kampala", "cape town"],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"{place.title()}")
    print()