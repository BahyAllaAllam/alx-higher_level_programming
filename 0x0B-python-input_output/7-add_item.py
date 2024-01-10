#!/usr/bin/python3
"""
Defining an empty class
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all command-line arguments to the list
for arg in sys.argv[1:]:
    items.append(arg)

# Save the updated list back to the file
save_to_json_file(items, filename)
