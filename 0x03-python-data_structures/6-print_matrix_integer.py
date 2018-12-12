#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    pos = 0
    count = 0
    for i in matrix:
        for elem in matrix[pos]:
            length = len(matrix[pos]) - 1
            if count < length:
                print("{:d}".format(elem), end=' ')
                count += 1
                continue
            print("{:d}".format(elem), end='')
            continue
        pos += 1
        count = 0
        print()
