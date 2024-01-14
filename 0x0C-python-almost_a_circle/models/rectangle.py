#!/usr/bin/python3
"""Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.\
            format(self.id, self.x, self.y, self.width,
                   self.height)

    @property
    def width(self):
        """Width of this rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.check_positive_integer(value, "width")
        self.__width = value

    @property
    def height(self):
        """Height of this rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.check_positive_integer(value, "height")
        self.__height = value

    @property
    def x(self):
        """x of this rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.check_positive_integer(value, "x")
        self.__x = value

    @property
    def y(self):
        """y of this rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.check_positive_integer(value, "y")
        self.__y = value

    @staticmethod
    def check_positive_integer(value, attribute_name):
        if type(value) != int or not isinstance(attribute_name, str):
            raise TypeError("{} must be an integer".format(attribute_name))
        elif value <= 0 and attribute_name in ["height", "width"]:
            raise ValueError("{} must be > 0".format(attribute_name))
        elif value < 0 and attribute_name in ["y", "x"]:
            raise ValueError("{} must be >= 0".format(attribute_name))

    def area(self):
        return self.__width * self.__height

    def display(self):
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def update(self, *args, **kwargs):
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.__width
            self.height = args[2] if len(args) >= 3 else self.__height
            self.x = args[3] if len(args) >= 4 else self.__x
            self.y = args[4] if len(args) >= 5 else self.__y
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
