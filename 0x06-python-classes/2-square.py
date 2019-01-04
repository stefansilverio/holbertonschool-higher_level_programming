#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Initialize a class.

        Args:
            param1: self
            param2: size

        Returns:
            None
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
