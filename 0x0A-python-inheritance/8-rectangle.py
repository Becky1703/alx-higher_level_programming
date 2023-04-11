#!/usr/bin/python3
"""Function that defines a class"""


class BaseGeometry:
    """an empty class"""
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if an argument is an integer.
        Raise:
           TypeError if value is not an integer.
           ValueError if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherited BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a rectangle class
        Takes two arguments - width and height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
