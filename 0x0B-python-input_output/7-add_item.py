#!/usr/bin/python3
"""
Defining an empty class
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_to_list_and_save(arguments):
    """Load existing items from file if it exists"""
    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []

    items.extend(arguments)

    save_to_json_file(items, 'add_item.json')


if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_to_list_and_save(arguments)
