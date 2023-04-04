#!/usr/bin/python3
"""Class Function LockedClass"""


class LockedClass:
    """Initializes a Locked class that prevents variable apart
    from first_name from being created

    """
    __slots__ = ["first_name"]
