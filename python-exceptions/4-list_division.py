#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for index in range(list_length):
        try:
            dividend = my_list_1[index] if index < len(my_list_1) else 0
            divisor = my_list_2[index] if index < len(my_list_2) else 1
            div_result = dividend / divisor

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
