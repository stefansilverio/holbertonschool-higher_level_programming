#!/usr/bin/python3
"""
Determine if obj is instance of class
Return:
Status
"""


def is_same_class(obj, a_class):
    """Return class status
    examine object
    """
    if type(obj) == a_class:
        return True
    else:
        return False
