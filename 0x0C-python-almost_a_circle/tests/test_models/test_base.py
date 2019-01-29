#!/usr/bin/python3
"""Unittest for base"""
import unittest
from models.base import Base


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
        dictionary = r1.to_dictionary()
        self.assertEqual(print(dictionary), {'x': 2, 'width': 10,
                                             'id': 1, 'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), "<class 'dict'>")
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(print(json_dictionary), [{"x": 2, "width":
                                                   10, "id": 1, "height": 7,
                                                   "y": 8}])
        self.assertEqual(type(json_dictionary), "<class 'str'>")
        json_dictionary = Base.to_json_string([])
        self.asserEqual(print(json_dictionary), "[]")

#  #16
    def test_str_fi(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[{"y": 8, "x": 2, "id": 1,\
"width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, \
"width": 2, "height": 4}]")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

#  #17
    def test_jsonst(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(print(list_output), "{'height': 4, 'width': 10,\
'id': 89}, {'height': 7, 'width': 1, 'id': 7}")
        self.assertEqual(type(list_output), "<class 'list'>")
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(print(list_output), "[]")

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
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, "[139785911764752] \
        [Rectangle] (1) 2/8 - 10/7")
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_rectangles_output, "[139785911764976] [Square] \
        (5) 0/0 - 5")
