#!/usr/bin/python3
"""
module 8-rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        class Square
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

        self.integer_validator("size", size)
