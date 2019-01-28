#!/usr/bin/python3
"""
Rectangle class inherits from base
Return:
Build rectangl
"""
from models.base import Base


class Rectangle(Base):
    """
    base class for project
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        build rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        if (type(width) != int):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if (type(height) != int):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x"""
        if (type(x) != int):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y"""
        if (type(y) != int):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return area"""
        return (self.width * self.height)

    def display(self):
        """display triangle as hashes"""
        for nl in range(self.y):
            print()
        for h in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """customize print fn"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """update rectangle"""
        if (len(args) is 0):
            if (len(kwargs) is 0):
                raise TypeError("missing 2 required positional arguments: \
                'width' and 'height'")
            for (k, v) in kwargs.items():
                if (k is 'id'):
                    self.id = v
                if (k is 'width'):
                    self.width = v
                if (k is 'height'):
                    self.height = v
                if (k is 'x'):
                    self.x = v
                if (k is 'y'):
                    self.y = v
        else:
            length = len(args)
            idx = 0
            if (length > idx):
                self.id = args[0]
                idx += 1
            if (length > idx):
                self.width = args[1]
                idx += 1
            if (length > idx):
                self.height = args[2]
                idx += 1
            if (length > idx):
                self.x = args[3]
                idx += 1
            if (length > idx):
                self.y = args[4]

    def to_dictionary(self):
        new = {}
        new['x'] = self.x
        new['y'] = self.y
        new['id'] = self.id
        new['height'] = self.height
        new['width'] = self.width
        return new
