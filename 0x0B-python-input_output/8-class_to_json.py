#!/usr/bin/python3
"""
Defining an empty class
"""


def class_to_json(obj):
    """Defining an empty class"""
    obj_dict = {}
    for attr in dir(obj):
        if not attr.startswith('__') and not callable(getattr(obj, attr)):
            value = getattr(obj, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                obj_dict[attr] = value
    return obj_dict
