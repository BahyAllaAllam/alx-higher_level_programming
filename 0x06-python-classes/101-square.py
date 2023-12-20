#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Define a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: length of a side of the square (default 0).
            position: tuple of 2 positive integers for
                        position (default (0, 0)).

        Raises:
            TypeError: if size is not an integer or
                            if position is not a tuple of 2 positive integers
            ValueError: if size is less than 0 or
                            if position contains non-positive integers
        """
        self.size = size
        self.position = position

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
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value: tuple of 2 positive integers for position.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
            ValueError: if value contains non-positive integers
        """
        if not isinstance(value, tuple) or \
           len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or \
           any(i < 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' character and position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

    def __str__(self):
        """Return string representation of the square."""
        string_repr = ''
        if self.__size == 0:
            string_repr += '\n'
        else:
            for i in range(self.__position[1]):
                string_repr += '\n'
            for i in range(self.__size):
                string_repr += ' ' * self.__position[0] \
                    + '#' * self.__size + '\n'
        return string_repr.rstrip()
