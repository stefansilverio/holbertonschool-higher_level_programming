#!/usr/bin/python3
"""
return square dict representation
"""
import unittest
from models.square import Square

class TestBaseClass(unittest.TestCase):
    def test_e(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(str(s1_dictionary), "{'id': 1, 'x': 2, 'size': 10, 'y': 1}")
        self.assertEqual((type(s1_dictionary)), "<class 'dict'>")

        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertEqual(s1 == s2, "False")
