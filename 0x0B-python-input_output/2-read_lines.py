#!/usr/bin/python3
"""
Read lines of a txt file
Print n lines
Return: Nothing
"""


def read_lines(filename="", nb_lines=0):
    """
    print n lines of a file
    """
    with open(filename) as f:
        if nb_lines <= 0 or nb_lines >= len(f.readlines()):
            print(f.read(), end="")

        else:
            with open(filename) as f:
                for line in range(nb_lines):
                    print(f.readline(), end="")
