#!/usr/bin/python3
"""Function to convert JSON to object"""
import json


def from_json_string(my_str):
    """The function converts Json reprensation of a string
    back to an object.
    """
    return json.loads(my_str)
