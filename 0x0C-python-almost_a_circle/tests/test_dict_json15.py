#!/usr/bin/python3
"""
serialize py dict
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):

    def test_e(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str(dictionary), "{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}")
        self.assertEqual((type(dictionary)), "<class 'dict'>")
        self.assertEqual(str(json_dictionary), str([{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]))
        self.assertEqual((type(json_dictionary)), "<class 'str'>")
