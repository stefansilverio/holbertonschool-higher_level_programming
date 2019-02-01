#!/usr/bin/python3
"""
Create square
Return:
Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """create square
        Return: nothing
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
