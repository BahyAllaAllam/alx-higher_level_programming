#!/usr/bin/python3
"""
Defining an empty class
"""


import json


def load_from_json_file(filename):
    """Defining an empty class"""
    with open(filename, 'r') as file:
        return json.load(file)
