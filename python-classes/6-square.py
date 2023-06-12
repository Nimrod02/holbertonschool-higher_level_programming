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
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size)**2

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
       if self.__size == 0:
           print()
       else:
            for _ in range(self.__position[1]):
               print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

