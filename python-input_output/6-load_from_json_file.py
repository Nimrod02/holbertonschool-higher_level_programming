#!/usr/bin/python3
"""
module 6-load_from_json_file
"""

import json


def load_from_json_file(filename):
    """load_from_json_file

    Args:
        filename (str): str filename
    """
    with open(filename) as file_open:
        data = json.load(file_open)
    return data
