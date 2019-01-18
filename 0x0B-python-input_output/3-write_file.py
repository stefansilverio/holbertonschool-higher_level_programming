#!/usr/bin/python3
"""
Write string to txt file
Return:
Number of chars written
"""


def write_file(filename="", text=""):
    """
    return number of chars written
    """
    with open(filename, "w+") as f:
        return f.write(text)
