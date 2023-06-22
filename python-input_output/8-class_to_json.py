#!/usr/bin/python3
"""
module 8-class_to_json
"""


def class_to_json(obj):
    """class_to_json

    Args:
        obj (dict): dictionary contain all the requirment for the task
    """
    return obj.__dict__
