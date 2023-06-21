#!/usr/bin/python3
"""
module 4-from_json_string
"""

import json


def from_json_string(my_str):
    """from_json_string

    Args:
        my_str (str): contain a string
    """
    return json.loads(my_str)
