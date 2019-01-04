#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        if len(position) == 2 and isinstance(position, tuple):
            self.__position = position
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) == 2 and isinstance(value, tuple):
            self.__position = value

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

    def my_print(self):
        count = idx = 0
        lines = self.__position[1]
        spaces = self.__position[0]
        while lines > 0:
            print('')
            lines -= 1
        while self.__size > count:
            spaces = self.__position[0]
            while spaces > 0:
                print(' ', end='')
                spaces -= 1
            idx = 0
            while self.__size > idx:
                print('#', end='')
                idx += 1
            print()
            count += 1
        if self.__size == 0:
            print()

    def area(self):
        if isinstance(self.__size, int) is not True:
            raise TypeError("size must be an integer")
        else:
            return self.__size**2
