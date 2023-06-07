#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for index in range(x):
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end="")
                count += 1
        print()
        return count

    except IndexError:
        print()
        return count

