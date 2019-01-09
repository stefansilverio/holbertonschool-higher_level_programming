#!/usr/bin/python3
"""
return sum of two integers
Returns:
sum of two integers
"""


def add_integer(a, b=98):
    """Add two integers.
    Returns:
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    try:
        return a + b
    except TypeError:
        if isinstance(b, int) is True:
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")
