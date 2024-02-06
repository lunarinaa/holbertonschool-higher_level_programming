#!/usr/bin/python3
"""Defining aRectangle Class"""


class Rectangle:
    """Empty class representing a rectangle

    Attribute:
        number_of_instances: The number of Rectangle instances
        print_symbol: Symbol used for representaion
    """

    number_of_instances = 0
    print_symbol = "#"

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the shape with greater area.

        Args:
        rect_1: the 1st rectangle
        rect_2: the 2nd rectangle
        Raises:
        TypeError: if one of the shapes is not Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
    
    @classmethod
    def square(cls, size=0):
        """Returns square
        Args: size - side of square
        """
        return cls(size, size)
