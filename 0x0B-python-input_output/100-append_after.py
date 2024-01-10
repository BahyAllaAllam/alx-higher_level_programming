#!/usr/bin/python3
"""
Defining an empty class
"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
