#!/usr/bin/python3
"""
 module 5 - text_indedation
"""


def text_indentation(text):
    """matrix_divided

    Args:
        text (): contain the text for the test
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delimiter in ".?:":
        text = text.replace(delimiter, delimiter + "\n\n")
    each_lines = [lines.strip(' ') for lines in text.split('\n')]
    new_line = "\n".join(each_lines)
    print(new_line, end="")
