#!/usr/bin/python3
"""Unittest for base"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    #  #1
    def test_id(self):
        b1 = Base()
        self.assertEqual(1, b1.id)
        b2 = Base()
        self.assertEqual(2, b2.id)
        b3 = Base(4)
        self.assertEqual(4, b3.id)
        b4 = Base(12)
        self.assertEqual(12, b4.id)
        b5 = Base()
        self.assertEqual(3, b5.id)
        b6 = Base("cat")
        self.assertEqual("cat", b6.id)
        with self.assertRaises(TypeError) as cm:
            b7 = Base(1, 2)
        self.assertEqual("__init__() takes from 1 to 2 \
positional arguments but 3 were given", str(cm.exception))

#  #15
    def test_jrep(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()  # convert obj to dict
        self.assertEqual(str(dictionary), "{'x': 2, 'width': 10,'id': 1,\
        'height': 7, 'y': 8}")  # check output

    def test_check_type(self):
        r1 = Rectangle(10, 7, 2, 8)  # create new obj
        dictionary = r1.to_dictionary()  # convert to dict
        self.assertEqual(type(dictionary), "<class 'dict'>")  # check type

    def test_check_opt(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])  # convert to json
        self.assertEqual(str(json_dictionary), [{"x": 2, "width":
                                                 10, "id": 1, "height": 7,
                                                 "y": 8}])

    def test_types(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])  # convert to json
        self.assertEqual(type(json_dictionary), "<class 'str'>")  # check conv

    def test_empty(self):
        json_dictionary = Base.to_json_string([])
        self.asserEqual(str(json_dictionary), "[]")

    def test_none(self):
        json_dictionary = Base.to_json_string(None)
        self.asserEqual(str(json_dictionary), "[]")

    def test_argc(self):
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle()  # invalid arg count
        self.assertEqual("__init__() missing 2 required positional\
        arguments: 'width' and 'height'", str(cm.exception))

    def test_argc(self):
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(2, 1, 4, 5, 2, 3)  # invalid arg count
        self.assertEqual("__init__() missing 2 required positional\
        arguments: 'width' and 'height'", str(cm.exception))

    def test_argty(self):
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle("3")  # invalid arg count
        self.assertEqual("width must be an integer", str(cm.exception))

    def test_argv(self):
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(-2)  # negative value for width
        self.assertEqual('width must be > 0', str(cm.exception))

#  test square shape

    def test_jrep(self):
        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()  # convert obj to dict
        self.assertEqual(str(dictionary), "{'size': 10,'x': 7,\
        'y': 2}")  # check output

    def test_check_type(self):
        r1 = Square(10, 7, 2)  # create new obj
        dictionary = r1.to_dictionary()  # convert to dict
        self.assertEqual(type(dictionary), "<class 'dict'>")  # check type

    def test_check_opt(self):
        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])  # convert to json
        self.assertEqual(str(json_dictionary), [{"size": 10, "x":
                                                 7, "y": 2}])

    def test_types(self):
        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])  # convert to json
        self.assertEqual(type(json_dictionary), "<class 'str'>")  # check conv

    def test_empty(self):
        json_dictionary = Base.to_json_string([])
        self.asserEqual(str(json_dictionary), "[]")

    def test_none(self):
        json_dictionary = Base.to_json_string(None)
        self.asserEqual(str(json_dictionary), "[]")

    def test_argc(self):
        with self.assertRaises(TypeError) as cm:
            r1 = Square()  # invalid arg count
        self.assertEqual("__init__() missing 1 required positional\
        argument: 'size'", str(cm.exception))

    def test_argty(self):
        with self.assertRaises(TypeError) as cm:
            r1 = Square("3")  # invalid arg count
        self.assertEqual("size must be an integer", str(cm.exception))

    def test_argv(self):
        with self.assertRaises(ValueError) as cm:
            r1 = Square(-2)  # negative value for width
        self.assertEqual('size must be > 0', str(cm.exception))

# both shapes, empty, none, invalid arg count, typeerrors

#  #16
    def test_match1(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{"y": 8, "x": 2,
                                                        "id": 1,
                                                        "width": 10,
                                                        "height": 7}])

    def test_match2(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{"y": 8, "x": 2,
                                                        "id": 1,
                                                        "width": 10,
                                                        "height":
                                                        7}, {"y":
                                                             0, "x":
                                                             0,
                                                             "id": 2,
                                                             "width":
                                                             2, "height":
                                                             4}])

    def test_teep(self):
        r1 = Rectangle(10, 7, 2)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(type(file.read()), "<class 'str'>")

    def test_emptn(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_non(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_overfl(self):
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(2, 3, 4, 5, 6, 1)
        self.assertEqual(str(cm.exception), "")

    def test_match1(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{"y": 8, "x": 2,
                                                        "id": 1,
                                                        "width": 10,
                                                        "height":
                                                        7}])

    def test_match2(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [{"y": 8, "x": 2,
                                                        "id": 1,
                                                        "width": 10,
                                                        "height":
                                                        7}, {"y": 0,
                                                             "x": 0,
                                                             "id": 2,
                                                             "width":
                                                             2, "height":
                                                             4}])

    def test_teep(self):
        r1 = Rectangle(10, 7, 2)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(type(file.read()), "<class 'str'>")

    def test_emptn(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_non(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_overfl(self):
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle()
        self.assertEqual(str(cm.exception), "__init__() missing 2 required\
        positional arguments: 'width' and 'height'")

# valid, invalid, empty, none, more than expected, both shapes

#  #17
    def test_jsonst(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
        ]
        json_list_input = Rectangle.to_json_string(list_input)  # make obj json
        list_output = Rectangle.from_json_string(json_list_input)  # make list
        self.assertEqual(str(list_output), "[{'height': 4, 'width': 10,\
        'id': 89}]")
        self.assertEqual(type(list_output), "<class 'list'>")

    def test_emp(self):
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(str(list_output), "[]")

    def test_mul(self):
        list_input = [
            {'id': 67, 'width': 1, 'height': 4},
            {'id': 89, 'width': 10, 'height': 4},
            ]
        json_list_input = Rectangle.to_json_string(list_input)  # make obj json
        list_output = Rectangle.from_json_string(json_list_input)  # make list
        self.assertEqual(str(list_output), "[{'height': 4, 'width': 10,\
        'id': 89}, {'height': 7, 'width': 1, 'id': 7}]")

    def test_jsonst(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
        ]
        json_list_input = Square.to_json_string(list_input)  # make obj json
        list_output = Square.from_json_string(json_list_input)  # make list
        self.assertEqual(str(list_output), "[{'height': 4, 'width': 10,\
        'id': 89}]")
        self.assertEqual(type(list_output), "<class 'list'>")

    def test_emp(self):
        list_input = []
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(str(list_output), "[]")

    def test_mul(self):
        list_input = [
            {'id': 67, 'width': 1, 'height': 4},
            {'id': 89, 'width': 10, 'height': 4},
            ]
        json_list_input = Square.to_json_string(list_input)  # make obj json
        list_output = Square.from_json_string(json_list_input)  # make list
        self.assertEqual(str(list_output), "[{'height': 4, 'width': 10,\
        'id': 89}, {'height': 7, 'width': 1, 'id': 7}]")

# multiple diictionaries, typeerrors, none, both shapes, invalid counts

#  #18
    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(print(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(print(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(print(r1 is r2), False)
        self.assertEqual(print(r1 == r2), False)
        r3 = Square(3, 4, 5)
        r3_dictionary = r3.to_dictionary()
        r4 = Square.create(**r3_dictionary)
        self.assertEqual(print(r3), "[Square] (1) 5/0 - 3/4")
        self.assertEqual(print(r4), "[Square] (1) 5/0 - 3/4")
        self.assertEqual(print(r3 is r4), False)
        self.assertEqual(print(r3 == r4), False)

#  #19
    def test_load(self):
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), "[Rectangle] (8)\
        2/8 - 10/7")

    def test_load_mul(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 2)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[1]), "[Rectangle] (6)\
        2/8 - 4/4")

    def test_load_sq(self):
        s1 = Square(5)
        list_squares_input = [s1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), "[Square] (5) 0/0 - 5")

    def test_load_square_mul(self):
        r1 = Square(10, 7, 2, 8)
        r2 = Square(10, 2)
        list_squares_input = [r1, r2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[1]), "[Square] (6) 2/8 - 4/4")

    def test_nop(self):
        list_squares_input = []
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), "[]")

    def test_opy(self):
        list_squares_input = None
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), "[]")

#  multiple instances, empty, none, overflow, types
#  one for each
