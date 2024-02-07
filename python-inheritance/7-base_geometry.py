#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    """Creates class"""

    def area(self):
        """Raises exeption message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
