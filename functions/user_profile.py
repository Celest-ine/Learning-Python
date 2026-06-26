def build_profile(first, last, **user_info):
    """A user profile of with first name, last name and 3 oter key value pairs."""
    
    profile = {
        'first_name': first,
        'last_name': last,
    }

    profile.update(user_info)

    return profile
def print_user_info(user_profile):
    for key, value in user_profile.items():
        formatted_key = key.replace('_', ' ')
        print(f'{formatted_key.title()}: {value}')

user_profile = build_profile('celestine', 'wangechi', age=25, favorite_color='black', country='kenya')
print_user_info(user_profile)