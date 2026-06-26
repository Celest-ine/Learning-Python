def build_profile(first, last, **user_info):
    """A user profile of with first name, last name and 3 oter key value pairs."""

    user_info[first_name] = first
    user_info[last_name] = last
    return user_info
user_profile = ('celestine', 'wangechi', 'age'=25, 'location'='nairobi', 'country'='kenya')
print(user_profile)