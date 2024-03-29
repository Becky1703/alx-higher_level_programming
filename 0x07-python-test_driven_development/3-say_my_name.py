#!/usr/bin/python3
"""Function that prints a formatted string"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints the names passed to it
    as arguments.

    Args:
       first_name is the first argument
       last_name is the second argument

    Returns:
    My name is <first name> <last name>
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
