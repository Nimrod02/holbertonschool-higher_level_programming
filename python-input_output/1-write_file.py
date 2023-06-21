#!/usr/bin/python3
"""
module 1-write_file
"""


def write_file(filename="", text=""):
    """write_file

    Args:
        filename (str)
        text (str)
    """
    with open(filename, 'w', encoding="utf-8") as file:
        read_file = file.write(text)
        return read_file
