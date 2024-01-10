#!/usr/bin/python3
"""
Defining an empty class
"""


def write_file(filename="", text=""):
    """Defining an empty class"""
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters
