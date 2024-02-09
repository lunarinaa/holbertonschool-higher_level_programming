#!/usr/bin/python3
"""Defines Pascals Triangle"""


def pascal_triangle(n):
    """Returns list of lists of integers representing Pascals triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) is not n:
        shape = triangle[-1]
        temp = [1]
        for i in range(len(shape) - 1):
            temp.append(shape[i] + shape[i + 1])
            temp.append(1)
            triangle.append(temp)
    return triangle
