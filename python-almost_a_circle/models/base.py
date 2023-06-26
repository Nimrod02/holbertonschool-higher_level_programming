#!/usr/bin/python3
"""
module base
"""


class Base:

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
