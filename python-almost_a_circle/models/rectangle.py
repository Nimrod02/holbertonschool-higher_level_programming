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
        for axes in range(self.y):
            print()

        for rows in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.__x) + "/" + str(self.__y) + " - "
        string += str(self.__width) + "/" + str(self.__height)
        return string

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args is not []:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'width' in kwargs:
            self.width = kwargs['width']
        if 'height' in kwargs:
            self.height = kwargs['height']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle

        Returns:
            dictionary: this dictionary contain the value of rectangle
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'width': self.width, 'height': self.height}
