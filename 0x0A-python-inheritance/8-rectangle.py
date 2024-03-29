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
