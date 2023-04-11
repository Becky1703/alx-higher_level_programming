#!/usr/bin/python3
"""Function that defines a class an inherited class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherited class Rectangle"""

    def __init__(self, size):
        """Initializes a square class
        Takes one argument - size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
