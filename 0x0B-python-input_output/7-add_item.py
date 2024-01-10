#!/usr/bin/python3
"""
Defining an empty class
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_to_list_and_save(arguments):
    try:
        # Load existing items from file if it exists
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []

    # Add new items from command-line arguments
    items.extend(arguments)

    # Save the updated list to add_item.json
    save_to_json_file(items, 'add_item.json')


if __name__ == "__main__":
    # Extract command-line arguments excluding the script name
    arguments = sys.argv[1:]

    # Add the arguments to the list and save to add_item.json
    add_to_list_and_save(arguments)
