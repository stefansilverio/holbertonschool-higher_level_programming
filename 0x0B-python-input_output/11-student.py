#!/usr/bin/python3
"""
create student class
Return:
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

    def to_json(self):
        """
        retrieve dict
        """
        return self.__dict__
