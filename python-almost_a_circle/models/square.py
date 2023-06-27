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

        Args:
            size (int): size of Square
            x (int): axe X. Defaults to 0.
            y (int): axe Y. Defaults to 0.
            id (int): id of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)


    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"


