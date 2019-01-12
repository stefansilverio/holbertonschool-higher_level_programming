#!/usr/bin/python3
"""
This function prints my name
Returns:
My name
"""


def say_my_name(first_name, last_name=""):
    """prints a name to stdout
    Returns name
    """
    if isinstance(first_name, str) is not True:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) is not True:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:1}{:2}".format(first_name, last_name))
