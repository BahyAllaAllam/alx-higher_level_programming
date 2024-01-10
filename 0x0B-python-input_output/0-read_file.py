#!/usr/bin/python3
"""
Defining an empty class
"""


def read_file(filename=""):
    """Defining an empty class"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
