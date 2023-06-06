#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary)
    for keys in sorted_list:
        print(f"{keys}: {a_dictionary[keys]}")
