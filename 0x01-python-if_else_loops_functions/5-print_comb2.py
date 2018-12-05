#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        print("{0:02}, ".format(i), end='')
    elif i == 99:
        print("{0}\n".format(i), end='')
