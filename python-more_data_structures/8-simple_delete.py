#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key is not None and a_dictionary is not None:
        return a_dictionary

    del a_dictionary[key]
    return a_dictionary
