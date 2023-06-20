#!/usr/bin/python3
"""
module 2-is_same_class
"""
def is_same_class(obj, a_class):
    """is_same_class

    Args:
        obj (int): comparison1
        a_class (int): comparison2

    Returns:
        _type_: the result of the comparison
    """
    return True if type(obj) is a_class else False
