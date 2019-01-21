#!/usr/bin/python3
"""
create student
Return:
none
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
        create dict
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

    def reload_from_json(self, json):
        """
        re-initialize data
        """
        if (bool(json) is False):
            pass
        else:
            self = json
