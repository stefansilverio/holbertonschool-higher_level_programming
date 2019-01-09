#!/usr/bin/python3
"""
This function divides all elements of a matrix
Returns:
New matrix
"""


def matrix_divided(matrix, div):
    """creates new matrix.
    Returns:
    New matrix
    """
    new_matrix = []

    length = len(matrix[0])   # save length of matrix

    if isinstance(matrix, list) is not True:
        raise TypeError("matrix must be a matrix (list of lists) of \
        integers/floats")

    if (isinstance(div, (int, float)) is not True):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for x in matrix:
        if isinstance(x, list) is not True:
            raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
        for y in x:
            if (isinstance(y, (int, float)) is not True):
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
            if length != len(x):
                raise TypeError("Each row of the matrix must have\
                the same size")
    new_matrix = [[round(i/div, 2) for i in j] for j in matrix]
    return new_matrix
