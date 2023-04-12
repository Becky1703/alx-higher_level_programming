#!/usr/bin/python3
"""Function that returns dictionary description"""


def class_to_json(obj):
    """The function returns the dictionary
    representation of the object
    """
    return obj.__dict__
