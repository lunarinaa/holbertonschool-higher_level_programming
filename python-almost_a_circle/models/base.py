#!/usr/bin/python3
"""Defines a class"""

class Base:
    """Class named Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects