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
    if (isinstance(div, (int, float)) is not True):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list) is not True:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        if isinstance(row, list) is not True:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for column in row:
            if (isinstance(column, (int, float)) is not True):
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
            new_list.append(round(column/div, 2))
        new_matrix.append(new_list)
    return new_matrix
