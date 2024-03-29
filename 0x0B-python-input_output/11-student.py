#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Class student initialized"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function gets dict representation of student"""
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Function to replace all attributes of Student"""
        for k, v in json.items():
            setattr(self, k, v)
