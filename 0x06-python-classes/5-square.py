#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        if isinstance(self.__size, int) is not True:
            raise TypeError("size must be an integer")
        else:
            return self.__size**2

    def my_print(self):
        count = idx = 0
        while self.__size > count:
            idx = 0
            while self.__size > idx:
                print('#', end='')
                idx += 1
            print()
            count += 1
        if self.__size == 0:
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
