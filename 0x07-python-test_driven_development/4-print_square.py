#!/usr/bin/python3
"""Function Print Square"""


def print_square(size):
    """
    A functin that prints a square of '#'
    It takes one argument 'size'

    Returns:
       The printed square
    """

    if type(size) is not int or size is None:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
