#!/usr/bin/python3
for number in range(0, 9):
    for inner in range(number + 1, 10):
        if (number != 8) or (inner != 9):
            print("{}{}, ".format(number, inner), end="")
        else:
            print("{}{}".format(number, inner))
