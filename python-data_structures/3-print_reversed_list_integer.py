#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for index in reversed(my_list):
        print("{:d}".format(index))
    if index < 0 or index >= len(my_list):
        return my_list
