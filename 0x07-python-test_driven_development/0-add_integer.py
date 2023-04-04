#!/usr/bin/python3
"""A python function that adds two integers"""


def add_integer(a, b=98):
    """This function adds and returns a + b

    """

    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
