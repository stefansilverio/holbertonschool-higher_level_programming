#!/usr/bin/python3
"""
read text file
prints to stdout
Returns: None
"""


def read_file(filename=""):
    """
    prints to stdout
    """
    with open(filename, "r") as f:
        print(f.read(), end="")
