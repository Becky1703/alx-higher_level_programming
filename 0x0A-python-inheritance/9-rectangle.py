#!/usr/bin/python3
"""Function that defines a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """function to return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return print() and str()"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
