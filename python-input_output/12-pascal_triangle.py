#!/usr/bin/python3
"""
module 12-pascal_triangle
"""


def pascal_triangle(n):
    """pascal_triangle

    Args:
        n (int): contain the value 5 for the triangle

    Returns:
        list: return triangle that is a list of list
    """
    triangle = []
    current_row = [1]
    if n <= 0:
        return triangle
    triangle.append(current_row)

    for rows in range(1, n):
        new_row = current_row + [1]
        for column in range(len(current_row) - 1):
            new_row[column + 1] = current_row[column] + current_row[column + 1]
        current_row = new_row

        triangle.append(current_row)

    return triangle
