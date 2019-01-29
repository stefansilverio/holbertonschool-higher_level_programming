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
            r1 = Rectangle("10", 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(10, "2")
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(10, 2, "3", 2)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(10, 2, 3, "2")
        self.assertEqual('y must be an integer', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(10, 2, -3, 2)
        self.assertEqual('x must be >= 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(10, 2, 3, -2)
        self.assertEqual('y must be >= 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(-10, 2, 3, 2)
        self.assertEqual('width must be > 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(10, -2, 3, 2)
        self.assertEqual('height must be > 0', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r2 = Rectangle()
        self.assertEqual("__init__() missing 2 required positional \
arguments: 'width' and 'height'", str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r2 = Rectangle(2)
        self.assertEqual("__init__() missing 1 required positional \
argument: 'height'", str(cm.exception))
