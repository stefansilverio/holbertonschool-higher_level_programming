#!/usr/bin/python3
"""
raise exception
Return:
exception w/ message
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """set values
        Return: Nothing
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """calc area
        Return: area
        """
        return self.__width * self.__height

    def __str__(self):
        """print function
        Return: thing you want to print
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
