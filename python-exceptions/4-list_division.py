#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    if not my_list_1 or not my_list_2 or not list_length:
        return None

    for index in range(list_length):
        try:
            div_result = my_list_1[index] / my_list_2[index]

        except TypeError:
            print("wrong type")
            div_result = 0

        except ZeroDivisionError:
            print("division by 0")
            div_result = 0

        except IndexError:
            print("out of range")
            div_result = 0

        finally:
            result.append(div_result)

    return result