#!/usr/bin/python3
"""Function that inherits int class"""


class MyInt(int):
    """class to invert int operators == and !=

    """
    def __eq__(self, value):
        """ Invert the == operator"""
        return self.real != value

    def __ne__(self, value):
        """Inverts the != operator"""
        return self.real == value
