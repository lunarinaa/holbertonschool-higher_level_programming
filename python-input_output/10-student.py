#!/usr/bin/python3
"""Defines a new class"""


class Student:
    """new classs"""

    def __init__(self, first_name, last_name, age):
        """Function than initializes a student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of Sudent"""
        if (type(attrs) is list and
                all(type(elem) is str for elem in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
