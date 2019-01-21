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
            f.seek(0)
            print(f.read(), end="")

        else:
            f.seek(0)
            for line in range(nb_lines):
                print(f.readline(), end="")
