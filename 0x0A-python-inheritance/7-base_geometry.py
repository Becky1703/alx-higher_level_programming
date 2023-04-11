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
           TypeError if valu is not an integer.
           ValueError if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
