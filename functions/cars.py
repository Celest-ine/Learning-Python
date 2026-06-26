def car(manufacture, model_name, **kwargs):
    """A function that stores information about a car in a dictionary."""

    car_info = {
        'manufacture': manufacture,
        'model name': model_name,
    }

    car_info.update(kwargs)

    return car_info

car_model = car('subaru', 'outback', color='blue', tow_package=True)
print(car_model)
car_model = car('kia', 'sportage', color='black', warrant=True)
print(car_model)