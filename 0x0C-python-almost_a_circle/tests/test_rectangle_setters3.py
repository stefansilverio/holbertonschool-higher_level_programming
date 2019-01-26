#!/usr/bin/python3
"""
Unittest for rectangle setters
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):

    def test_e(self):
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(10, "2")
        self.assertEqual('height must be an integer', str(cm.exception))

    def test_eq(self):
        with self.assertRaises(ValueError) as cm:
            r2 = Rectangle(10, 2)
            r2.width = -10
        self.assertEqual('width must be > 0', str(cm.exception))

    def test_equ(self):
        with self.assertRaises(TypeError) as cm:
            r3 = Rectangle("2")
        self.assertEqual("__init__() missing 1 required positional argument: 'height'", str(cm.exception))

    def test_equa(self):
        with self.assertRaises(TypeError) as cm:
            r4 = Rectangle(10)
        self.assertEqual("__init__() missing 1 required positional argument: 'height'", str(cm.exception))

    def test_equal(self):
        with self.assertRaises(ValueError) as cm:
            r5 = Rectangle(10, 2, -1, 2)
        self.assertEqual('x must be >= 0', str(cm.exception))

    def test_equals(self):
        with self.assertRaises(ValueError) as cm:
            r6 = Rectangle(10, 2, 3, -1)
        self.assertEqual('y must be >= 0', str(cm.exception))

if __name__ == '__main__':
    unittest.main()
