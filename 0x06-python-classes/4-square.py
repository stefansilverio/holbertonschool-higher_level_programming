#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        """
        Args:
            param1: self.
            param2: size.

        Returns:
            Returns area
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        if isinstance(self.__size, int) is not True:
            raise TypeError("size must be an integer")
        else:
            return self.__size**2
