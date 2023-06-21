#!/usr/bin/python3
"""
module 3-to_json_string
"""


def to_json_string(my_obj):
    """to_json_string

    Args:
        my_obj (json):

    Returns:
        json to string
    """
    import json

    return json.dumps(my_obj)
