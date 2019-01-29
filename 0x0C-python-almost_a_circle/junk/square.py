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
                if k == "id":
                    self.__dict__[k] = v
                elif k == "size":
                    self.width = v
                else:
                    self.__dict__['_Rectangle__{}'.format(k)] = v

        else:
            l = ['size', 'x', 'y']
            idx = 0
            bound = len(args)
            if bound > 1:
                self.width = args[1]
            self.__dict__['id'] = args[0]
            for elem in range(1, bound):
                self.__dict__['_Rectangle__{}'.format(l[idx])] = args[elem]
                idx += 1

    def to_dictionary(self):
        new = {}
        new['id'] = self.id
        new['size'] = self.width
        new['x'] = self.x
        new['y'] = self.y
        return new
