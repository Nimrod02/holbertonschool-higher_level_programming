#!/usr/bin/python3
"""
module 3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class

    Args:
        obj (int): comparison1
        a_class (int): comparison2

    Returns:
        _type_: the result of the comparison
    """
    return True if type(obj) is a_class or \
        issubclass(type(obj), a_class) else False
