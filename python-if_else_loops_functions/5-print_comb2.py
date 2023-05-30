#!/usr/bin/python3
print(", ".join("0" + str(num) if num < 10 else str(num)for num in range(100)))
