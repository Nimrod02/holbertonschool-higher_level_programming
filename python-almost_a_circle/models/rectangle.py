#!/usr/bin/python3
"""
module 2-rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class
    give a rectangle

    Args:
        Base (class): base class that rectangle inherite
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """define the axes and the width and height

        Args:
            width (int): width of the rectangle
            height (int): height
            x (int, optional): axes x. Defaults to 0.
            y (int, optional): axes y. Defaults to 0.
            id (int, optional): id from Basqse class. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
