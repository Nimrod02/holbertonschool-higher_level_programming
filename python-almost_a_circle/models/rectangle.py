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
    print_symbol = "#"

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """determine the area of rectangle

        Returns:
            int: area of the rectangle
        """
        return (self.__height * self.__width)

    def display(self):
        """
        display the rectangle
        """
        for rows in range(self.height):
                print("#" * self.width)
