#!/usr/bin/python3
"""
Defining an empty class
"""


import json


def save_to_json_file(my_obj, filename):
    """Convert the object to a JSON string"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
