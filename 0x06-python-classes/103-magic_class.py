#!/usr/bin/python3
"""Represents a class that emulates the given bytecode functionality."""


import math


class MagicClass:
    """Represents a class that emulates the given bytecode functionality."""

    def __init__(self, radius=0):
        """Constructor for MagicClass.

        Args:
            radius: number (float or integer) representing
                    the radius of the circle (default 0).

        Raises:
            TypeError: if radius is not a number (float or integer)
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.__radius
