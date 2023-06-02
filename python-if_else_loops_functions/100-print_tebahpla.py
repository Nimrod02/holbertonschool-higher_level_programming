#!/usr/bin/python3
for index in range(122, 96, -1):
    print("{}".format(chr(index)) if index % 2 == 0 else chr(index-32), end='')
