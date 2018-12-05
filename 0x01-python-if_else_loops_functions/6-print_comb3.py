#!/usr/bin/python3
for i in range(0, 9):  # first digit
    for a in range(i + 1, 10):  # second digit
        if i == 8:
            print("{0}{1}".format(i, a))
            break
        print("{0:01}{1}, ".format(i, a), end='')
