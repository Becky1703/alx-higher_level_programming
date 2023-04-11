#!/usr/bin/python3
"""Function that determines if an object is a given class"""


def is_same_class(obj, a_class):
    """The function checks if object is an instance
    of a specified class
    It takes two arguments obj, a_class.
    Returns:
         True if object is exactly an instance of given class
         False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
