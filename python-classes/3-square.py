#!/usr/bin/python3
"""
    module 2-square
"""


class Square:
    """
    class Square make the square

    Args:
        size : size of square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size)**2