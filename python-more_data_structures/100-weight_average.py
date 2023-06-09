#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        res = 0
        recurrence = 0
        for index in my_list:
            (weight, occurrence) = index
            res += (weight * occurrence)
            recurrence += occurrence
        return (res / recurrence) if recurrence > 0 else 0
    else:
        return 0
