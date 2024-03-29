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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation"""
        if list_dictionaries is None:
            return "[]"
        dicty = json.dumps(list_dictionaries)
        return dicty

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of instances to a JSON file"""
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        file_name = f"{class_name}.json"

        dict_list = [obj.to_dictionary() for obj in list_objs]
        json = cls.to_json_string(dict_list)
        with open(file_name, 'w') as file:
            file.write(json)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of JSON representetation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create"""
        if dictionary and dictionary is not {}:
            if cls.__name__ == "Rectangle":
                create = cls(1, 1)
            else:
                create = cls(1)
            create.update(**dictionary)
            return create

    @classmethod
    def load_from_file(cls):
        """List of classes from file"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
