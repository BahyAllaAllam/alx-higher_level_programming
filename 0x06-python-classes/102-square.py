#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a side of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: length of a side of the square.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator based on square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Non-equality comparator based on square area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator based on square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator based on square area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparator based on square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator based on square area."""
        return self.area() <= other.area()
