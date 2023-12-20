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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

     @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or
        len(value) != 2 or
        not all(isinstance(i, int) for i in value) or
        not all(i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
