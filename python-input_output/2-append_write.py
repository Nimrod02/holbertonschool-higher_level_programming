#!/usr/bin/python3
"""
module 2-append_file
"""


def append_write(filename="", text=""):
    """append_write

    Args:
        filename (str, optional): contain the name of the new file".
        text (str): text need to be append a the end of the file.

    Returns:
        the number of char append
    """
    with open(filename, "a", encoding="utf-8") as file:
        append = file.write(text)
    return append
