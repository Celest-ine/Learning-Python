def car(manufacture, model_name, **kwargs):
    """A function that stores information about a car in a dictionary."""

    car_info = {
        'manufacture': manufacture,
        'model name': model_name,
    }

    car_info.update(kwargs)

    return car_info

def print_car_info(car_model):
    """Print the car information in a user friendly way"""

    for key, value in car_model.items():
        print(f"{key.title()}: {value}")

car_model = car('subaru', 'outback', color='blue', tow_package=True)
print_car_info(car_model)
print()
car_model = car('kia', 'sportage', color='black', warrant=True)
print_car_info(car_model)