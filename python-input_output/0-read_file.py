#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        for lines in f:
            print(lines, end="")
