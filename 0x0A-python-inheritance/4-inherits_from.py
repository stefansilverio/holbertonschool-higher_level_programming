#!/usr/bin/python3
"""
Fn returns obj status
Returns:
Status
"""


def inherits_from(obj, a_class):
    """Return status
    Examine obj status
    """
    return isinstance(obj, a_class) and type(obj) != a_class
