#!/usr/bin/python3
"""
module 4-inherits_from
"""


def inherits_from(obj, a_class):
    """inherits_from

    Args:
        obj (int): comparison1
        a_class (int): comparison2

    Returns:
        _type_: the result of the comparison
    """
    return True if issubclass(type(obj), a_class) and type(obj) != a_class else False
