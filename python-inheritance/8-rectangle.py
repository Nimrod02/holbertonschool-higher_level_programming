#!/usr/bin/python3
"""
module 8-rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
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
