#!/usr/bin/python3
"""
create rectangle
Return:
rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """create rectangle
        Return: rectangle
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """print fn
        print this
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
