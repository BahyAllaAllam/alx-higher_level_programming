#!/usr/bin/python3
"""
Defines LockedClass that only allowed to create the first name instance
"""


class LockedClass:
    """LockedClass that only allowed to create the first name instance"""

    __slots__ = ('first_name',)
