#!/usr/bin/python3
"""
module base
"""

import json


class Base:
    """
    base class
    will be use for all class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor

        Args:
            id (int, None): Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """eturns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (dictionary): contain a string in json format

        Returns:
            dictionary: the python string of the dictionary
        """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): is a list of instances who inherits of Base
        """
        filename = type(list_objs[0]).__name__ + ".json"
        json_file = open(filename, "w")
        if list_objs is None:
            list_objs = []
            json.dump([], json_file)

        if type(list_objs[0]).__name__ == "Rectangle":
            new_dict = [item.to_dictionary() for item in list_objs]
            json_string = cls.to_json_string(new_dict)
            json.dump(new_dict, json_file)

        json_file.close()
