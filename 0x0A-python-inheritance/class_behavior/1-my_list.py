#!/usr/bin/python3
"""
This function sorts and prints a list
Returns:
None
"""


class MyList(list):
    """sorts list
    prints list
    """
    def print_sorted(self):
        i_copy = self.copy()
        i_copy.sort()
        print(i_copy)
