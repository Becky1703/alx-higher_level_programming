#!/usr/bin/python3
"""Function that inherits a superclass list"""


class MyList(list):
    pass

    def print_sorted(self):
        """prints the sorted list in ascending order"""
        print(sorted(self))
