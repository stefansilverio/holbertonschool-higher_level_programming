#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    pos = 0
    count = 0
    for i in matrix:
        for elem in matrix[pos]:
            if count == 2:
                print("{:d}".format(elem), end='')
                count += 1
                continue
            count += 1
            print("{:d}".format(elem), end=' ')
        pos += 1
        count = 0
        print()
