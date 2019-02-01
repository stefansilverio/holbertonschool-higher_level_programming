#!/usr/bin/python3
"""
Fn determines if obj is instance\
or if obj is subclass of a_class
Return: status
"""


def is_kind_of_class(obj, a_class):
    """Determine obj status
    Return obj status
    """
    if isinstance(obj, a_class):
        return True
    if issubclass(type(obj), a_class):
        return True
    return False
