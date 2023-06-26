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
        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x

    @property
    def width(self):
        return self.width

    @property
    def height(self):
        return self.height

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    @width.setter
    def width(self, value):
        self.width = value

    @height.setter
    def height(self, value):
        self.height = value

    @x.setter
    def x(self, value):
        self.x = value

    @y.setter
    def y(self, value):
        self.y = value
