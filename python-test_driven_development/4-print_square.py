#!/usr/bin/python3
"""
module 4-print_square
"""


def print_square(size):
    """print_square

    Args:
        size: size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for inddex in range(size):
        print("#" * size)
