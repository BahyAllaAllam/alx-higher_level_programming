#!/usr/bin/python3
"""
Defining an empty class
"""


def append_write(filename="", text=""):
    """Defining an empty class"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
