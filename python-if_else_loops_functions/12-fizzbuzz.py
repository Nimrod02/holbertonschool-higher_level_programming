#!/usr/bin/python3
def fizzbuzz():
    for f in range(1, 101):
        if f % 15 == 0:
            print("FizzBuzz", end=" ")
        elif f % 5 == 0:
            print("Buzz", end=" ")
        elif f % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{}".format(f), end=" ")
        if f == 100:
            continue
