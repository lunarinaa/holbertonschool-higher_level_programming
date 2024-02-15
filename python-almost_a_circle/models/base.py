#!/usr/bin/python3
"""Defines a class"""
import json


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

    def to_json_string(list_dictionaries):
        """Json representation"""
        if list_dictionaries is None:
            return []
        dicty = json.dumps(list_dictionaries)
        return dicty
