#!/usr/bin/python3
"""
module 0-read_file
"""


def read_file(filename=""):
    """read_file

    Args:
        filename (str, optional): contain the file of the test.
    """
    with open(filename) as f:
        for lines in f:
            print(lines, end="")
