#!/usr/bin/python3
"""
module 1-my_list
"""

class MyList(list):
    """My_list class

    Args:
        list (int): contain a list of int
    """
    def print_sorted(self):
        print(sorted(self))
