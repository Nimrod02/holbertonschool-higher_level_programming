#!/usr/bin/python3
def weight_average(my_list=[]):
    try:
        sum = 0
        for sub in my_list:
            for index in sub:
                sum = sum + index
        res = sum / len(my_list)
        return res
    except TypeError:
        pass
