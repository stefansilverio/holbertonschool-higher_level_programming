#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        new_list = []
        for row in matrix:
                new_list.append([x**2 for x in row])
        return new_list
