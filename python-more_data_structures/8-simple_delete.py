#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key is not None and a_dictionary is not None:
        return a_dictionary

    a_dictionary.pop(key)
    return a_dictionary
