#!/usr/bin/python3
"""
raise exception
Return:
exception w/ message
"""


class BaseGeometry:

    def area(self):
        """raise exception
        with message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value
        check value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer"
                            .format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0"
                             .format(name))
