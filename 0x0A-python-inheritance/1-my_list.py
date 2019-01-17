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
        self = self.copy()
        self.sort()
        print(self)
