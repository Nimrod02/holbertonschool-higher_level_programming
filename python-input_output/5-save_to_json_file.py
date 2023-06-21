#!/usr/bin/python3
"""
module 5-save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file

    Args:
        my_obj (dict): contain all the list
        filename (str): open file name

    Returns:
        _type_: _description_
    """
    with open(filename, "w", encoding="utf-8") as open_file:
        return (json.dump(my_obj, open_file))
