#!/usr/bin/python3
"""
create pascals triangle
Return:
Implementation of pascals triangle
"""


def pascal_triangle(n):
    """
    build pascal's triangle
    """
    big_list = []
    curr = [1, 1]
    sub_list = [1, 1]

    if (n <= 0):
        return big_list

    if (n >= 1):
        big_list.append([1])

    if (n >= 2):
        big_list.append([1, 1])

    for i in range(n):
        for elem in range(len(sub_list) - 1):
            curr.insert(1, sub_list[elem] + sub_list[elem + 1])
        sub_list = curr
        curr = [1, 1]
        big_list.append(sub_list)
    return big_list
