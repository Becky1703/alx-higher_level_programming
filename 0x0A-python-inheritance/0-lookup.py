#!/usr/bin/python3
"""Function that returns list of available attributes of object"""


def lookup(obj):
    """returns the list of available attributes to an object"""
    return (dir(obj))
