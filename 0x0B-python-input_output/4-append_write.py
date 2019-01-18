#!/usr/bin/python3
"""
append string to end of file
Return:
number of strs added
"""


def append_write(filename="", text=""):
    """
    Return num of strs added
    """
    with open(filename, "a") as f:
        return f.write(text)
