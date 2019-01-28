#!/usr/bin/python3
"""
square class inherits
from rectangle
Returns: Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, size):
        """set size"""
        self.width = size
        self.height = size

    def __str__(self):
        """override print fn"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    def update(self, *args, **kwargs):
        """update dict"""
        if (len(args) is 0):
            if (len(kwargs) is 0):
                raise TypeError("missing 2 required positional arguments: \
                'width' and 'height")
            for (k, v) in kwargs.items():
                if (k is 'id'):
                    self.id = v
                if (k is 'size'):
                    self.width = v
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
                self.height = args[1]
                idx += 1
            if (length > idx):
                self.x = args[2]
                idx += 1
            if (length > idx):
                self.y = args[3]

    def to_dictionary(self):
        new = {}
        new['id'] = self.id
        new['size'] = self.width
        new['x'] = self.x
        new['y'] = self.y
        return new
