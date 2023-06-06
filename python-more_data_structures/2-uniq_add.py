#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_value = set()

    for num in my_list:
        uniq_value.add(num)

    uniq_sum = sum(uniq_value)

    return uniq_sum
