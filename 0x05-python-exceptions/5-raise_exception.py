#!/usr/bin/python3
def raise_exception():
    try:
        unsupported_type = {}
        unsupported_type[()] = 42

    except TypeError as e:
        raise e
