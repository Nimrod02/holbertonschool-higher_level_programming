#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    for index in range(1, len(sys.argv)):
        res += int(sys.argv[index])
    print("{}".format(res))
