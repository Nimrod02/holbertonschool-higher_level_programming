#!/usr/bin/python3
"""module 1 divided matrix
"""


def matrix_divided(matrix, div):
    """matrix_divided

    Args:
        matrix (): matrix
        div (): div, rounded to 2 decimal places
    """
    errormessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errormessage)
    if not isinstance(matrix, list):
        raise TypeError(errormessage)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errormessage)
        for index in lists:
            if not isinstance(index, (int, float)):
                raise TypeError(errormessage)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errormessage)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise TypeError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
