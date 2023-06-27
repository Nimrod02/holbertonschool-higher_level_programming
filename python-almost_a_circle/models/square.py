#!/usr/bin/python3
"""
module square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Args:
        Rectangle (class): parent class of parent
    """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor of square
cd mode
        Args:
            size (int): size of Square
            x (int): axe X. Defaults to 0.
            y (int): axe Y. Defaults to 0.
            id (int): id of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args is not []:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'width' in kwargs:
            self.width = kwargs['width']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']
