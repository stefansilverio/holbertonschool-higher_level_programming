#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 1
    length = len(sys.argv)
    if length == 1:
        print("{0} arguments.".format(length - 1))
    elif length == 2:
        print("{0} argument:".format(length - 1))
        print("{0}: {1}".format(length - 1, sys.argv[1]))
    else:
        print("{0} arguments:".format(length - 1))
        for i in range(a, length):
            print("{0}: {1}".format(i, sys.argv[i]))
