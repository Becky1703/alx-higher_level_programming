#!/usr/bin/python3
"""Function that defines if object is an instance of a class or inherited"""


def inherits_from(obj, a_class):
    """Checks if object was inherited or not
    Takes two arguments obj, a_class
    Returns:
       True if inherited
       False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
