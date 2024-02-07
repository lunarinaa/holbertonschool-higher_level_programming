#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    """Creates class"""

    def area(self):
        """Raises exeption message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """Derived class"""

    def __init__(self, width, height):
        """Initialize sides of the rectangle"""
        self.__width = width
        self.__height = height
