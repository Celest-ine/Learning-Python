def car(manufacture, model_name, **kwargs):
    """A function that stores information about a car in a dictionary."""

    car[manufacture] = manufacture
    car[model_name] = model_name
    return car

car_model = ('subaru', 'outback', color='blue', tow_package=True)
car_model = ('kia', 'sportage', color='black', warrant=True)