#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = set(set_1)
    for s in set_1:
        res = res.symmetric_difference(set_2)
    return res
