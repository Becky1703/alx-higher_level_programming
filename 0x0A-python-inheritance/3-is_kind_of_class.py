#!/usr/bin/python3
"""Function that defines if object is an instance of class"""


def is_kind_of_class(obj, a_class):
    """returns True if object is an instance or was inherited
    it takes two arguments- obj, a_class
    Returns:
        True if object is an instance or inherited instance
        False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
