#!/usr/bin/python3
"""
student class
Returns:
None
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
        initialize data
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieve dict
        """
        if isinstance(attrs, list):
            for elem in attrs:
                if isinstance(elem, str):
                    continue
                else:
                    return self.__dict__

            new_dict = {k: v for k, v in self.__dict__.items() if k in attrs}
            return new_dict

        else:
            return self.__dict__
