#!/usr/bin/python3
"""
module 6-base_geometry
"""


class BaseGeometry:
    """
    class baseGeometry
    """
    def area(self):
        """area

        Raises:
            Exception: raise an error if execption
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Resume:
            Verify if value is a interger

        Args:
            -name: always string, the name of Geometry.
            -value: interger to ckeck
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
