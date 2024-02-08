#!/usr/bin/python3
"""Defines a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Derived class"""

    def __init__(self, width, height):
        """Initialize sides of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
