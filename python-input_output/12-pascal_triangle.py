#!/usr/bin/python3


def pascal_triangle(n):
    prev_line = [1]
    if n <= 0:
        return []

    for rows in range(n):
        new_line = prev_line + [1]
        for columns in range(len(prev_line) - 1):
            new_line[columns + 1] = prev_line[columns] + prev_line[columns + 1]
        prev_line = new_line
        print(new_line)
