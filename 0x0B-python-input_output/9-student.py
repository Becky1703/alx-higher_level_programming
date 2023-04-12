#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Class student initialized"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function gets dict representation of student"""
        return self.__dict__
