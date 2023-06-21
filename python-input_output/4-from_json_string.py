#!/usr/bin/python3
"""
module 4-from_json_string
"""


def from_json_string(my_str):
    import json
    """from_json_string

    Args:
        my_str (str): contain a string
    """
    return json.loads(my_str)
