#!/usr/bin/python3
"""Function to convert string to JSON representation"""
import json


def to_json_string(my_obj):
    """The function converts a object (string)
    and returns the JSON representation.
    """
    return json.dumps(my_obj)
