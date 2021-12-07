def build_profile(first, second, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["complexion"] = first
    user_info['course'] = second
    return user_info
"""inputing the arguments"""
user_profile = build_profile('Fair', 'Programming',
first_name='Udeme',
last_name='Umana')

print(user_profile)

def build_car(colour,kind, **car_info):
    """Build a dictioary containing everything you know about a car"""
    car_info["Color"] = colour
    car_info["Twopackage"] = kind
    return car_info
"""inputing the arguments inside"""
car_profile = build_car("Blue","True",Manufacture='Udeme', Model="Slam4")

print(car_profile)

