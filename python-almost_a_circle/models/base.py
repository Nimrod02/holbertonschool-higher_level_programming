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

    def to_json_string(list_dictionaries):
        """eturns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (dictionary): contain a string in json format

        Returns:
            dictionary: the python string of the dictionary
        """
        if list_dictionaries is None or list_dictionaries is []:
            list_dictionaries = []
            return list_dictionaries
        else:
            return json.dumps(list_dictionaries)
