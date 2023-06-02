#!/usr/bin/python3
def remove_char_at(str, n):
    n = abs(n)
    front = str[:n]
    back = str[n+1:]
    return front + back
