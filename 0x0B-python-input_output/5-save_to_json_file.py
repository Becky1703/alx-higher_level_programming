#!/usr/bin/python3
"""Function to write object to a text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """The function writes an object to a text file
    using a JSON representation
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
