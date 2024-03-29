#!/usr/bin/python3
"""Defining aRectangle Class"""


class Rectangle:
    """Empty class representing a rectangle

    Attribute:
        number_of_instances: The number of Rectangle instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle.

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """determine the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """determines the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Calculates perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Prints rectangle with # character"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """The string representation of an object"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """Printing message when delete rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
