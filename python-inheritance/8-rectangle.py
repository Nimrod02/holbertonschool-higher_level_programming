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

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
        """
            class baseGeometry
        """
        def __init__(self, width, height):
            """Rectangle init

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
            """
            self.__width = width
            self.__height = height

            self.integer_validator("width", self.__width)
            self.integer_validator("height", self.__height)
