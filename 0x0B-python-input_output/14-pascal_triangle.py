#!/usr/bin/python3
"""
this function builds
pascals triangl
Return: list of lists
"""


def pascal_triangle(n):
    """
    Return: list of lists
    """
    sub_list = []
    big_list = []
    num = 11
    ex = 0
    for i in range(n):
        result = 11**ex
        string = str(result)
        ex += 1
        for c in string:
            sub_list.append(c)
        big_list.append(sub_list)
        sub_list = []
    return big_list
