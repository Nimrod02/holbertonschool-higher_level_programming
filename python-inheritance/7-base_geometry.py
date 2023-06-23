#!/usr/bin/python3
"""Write a class BaseGeometry (based on 5-base_geometry.py)."""


class BaseGeometry:
    """class geometry"""

    def area(self):
        """return exception of area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
