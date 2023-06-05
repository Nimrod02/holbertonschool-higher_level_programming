#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string
    return("".join for c in new_string if c not in "Cc")
