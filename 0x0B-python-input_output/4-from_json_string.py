#!/usr/bin/python3
"""
Defining an empty class
"""


import json


def from_json_string(my_str):
    """Convert the JSON string to a Python object"""
    return json.loads(my_str)
