#!/usr/bin/python3
"""Function that reads a text"""


def read_file(filename=""):
    """the function reads a text from file and prints to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
