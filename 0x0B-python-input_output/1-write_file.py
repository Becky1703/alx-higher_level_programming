#!/usr/bin/python3
"""Function that writes string and returns number of characters"""


def write_file(filename="", text=""):
    """The function writes a string to a text file
    and returns the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
