#!/usr/bin/python3
"""
This function creates a rectangle
Returns:
specs
"""


class Rectangle:
    """Defines rectangle
    Returns specs
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.number_of_instances += 1
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ''
        new_string = ''
        for i in range(self.height):
            for y in range(self.width):
                if isinstance(self.print_symbol, str) is not str:
                    self.print_symbol = str(self.print_symbol)
                new_string = new_string + self.print_symbol
            if i is not max(range(self.height)):
                new_string = new_string + '\n'
        return new_string

    def __repr__(self):
        return ("Rectangle({:1},{:2})".format(2, 4))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
