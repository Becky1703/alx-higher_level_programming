#!/usr/bin/python3
"""Function to append"""


def append_write(filename="", text=""):
    """The function appends a string at the end of a text file
    and returns the number of charactere added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
