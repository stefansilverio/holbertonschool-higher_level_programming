#!/usr/bin/python3
"""
print number of lines
Return:
number of lines
"""


def number_of_lines(filename=""):
    """
    Print number of lines
    """
    with open(filename) as f:
        return len(f.readlines())
