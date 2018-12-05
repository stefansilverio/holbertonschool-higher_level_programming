#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    idx = 1
    length = len(sys.argv)
    if length == 1:
        print("{}".format(length - 1))
    else:
        for i in range(idx, length):
            sum += int(sys.argv[i])
        print("{}".format(sum))
