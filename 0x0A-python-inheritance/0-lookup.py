#!/usr/bin/python3
"""
This function creates list of atts
Returns:
list
"""


def lookup(obj):
    """Creates list
    Returns list
    """
    new_list = []
    for elem in dir(obj):
        new_list.append(elem)
    return new_list
