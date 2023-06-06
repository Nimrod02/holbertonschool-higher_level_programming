#!/usr/bin/python3
def common_elements(set_1, set_2):
    for char in set_1:
        for same in set_2:
            if char == same:
                return char
