#!/usr/bin/python3

import json


class Base:
    """base class for project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """count object"""
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to json obj"""
        if (len(list_dictionaries) is False or list_dictionaries is None):
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)
            return json_str

    @staticmethod
    def from_json_string(json_string):
        if (len(json_string) == 0 or json_string is None):
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        if (list_objs is None):
            with open("{}.json".format(cls.__name__), "w") as f:
                f.write(to_json_string([]))
        else:
            new = []
            with open("{}.json".format(cls.__name__), "w") as f:
                for obj in list_objs:
                    new.append(obj.to_dictionary())
                f.write(Base.to_json_string(new))

    @classmethod
    def create(cls, **dictionary):
        if (cls.__name__ == "Square"):
            dum = cls(4, 4, 4, 4)
        if (cls.__name__ == "Rectangle"):
            dum = cls(4, 4, 4, 4, 4)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        new = []
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                dic = Base.from_json_string(f.read())
                for i in dic:
                    new.append(cls.create(**i))
                return new
        except Exception:
            return []
