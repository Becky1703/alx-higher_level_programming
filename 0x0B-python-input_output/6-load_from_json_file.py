#!/usr/bin/python3
"""Function to create object from json file"""
import json


def load_from_json_file(filename):
    """The function creates an object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
