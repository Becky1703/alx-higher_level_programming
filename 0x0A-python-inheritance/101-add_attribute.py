#!/usr/bin/python3
"""Function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """The function adds an attribute to an object if possible.
    It takes three arguments - obj, att, and value
    Raises a TypeError if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
