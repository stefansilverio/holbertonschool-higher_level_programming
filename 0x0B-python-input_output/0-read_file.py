#!/usr/bin/python3
"""
read txt file
print to stdout
Return: None
"""


def read_file(filename=""):
    """
    print to stdout
    """
    with open(filename, "r") as f:
        print(f.read(), end="")
