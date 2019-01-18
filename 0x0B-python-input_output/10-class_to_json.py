#!/usr/bin/python3
"""
simple data structure
Return:
dictionary description
"""


def class_to_json(obj):
    """
    return dict
    """
    return obj.__dict__
