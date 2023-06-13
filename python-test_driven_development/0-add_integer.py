#!/usr/bin/python3
"""
module 0-add_int
"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a is isinstance(int, float) or b is isinstance(int, float):
        a = int(a)
        b = int(b)
    return int(a + b)

