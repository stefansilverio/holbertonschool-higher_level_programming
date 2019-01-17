#!/usr/bin/python3
"""
Invert equality sign
Return:
Values
"""


class MyInt(int):
    def __init__(self, num):
        """assign size
        assign size
        """
        self.num = num

    def __eq__(self, other):
        """invert equality
        invert
        """
        return self.num != other

    def __ne__(self, other):
        """invert equality
        invert
        """
        return self.num == other
