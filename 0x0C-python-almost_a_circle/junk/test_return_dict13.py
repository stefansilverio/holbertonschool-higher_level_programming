#!/usr/bin/python3
"""
return dictionary representation of rect
"""
import unittest
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    def test_e(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(isinstance(r1_dictionary, dict), True)
        self.assertEqual(str(r1_dictionary), "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}")
        self.assertEqual(str(type(r1_dictionary)), "<class 'dict'>")
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertEqual(str(r1 == r2), "False")
