#!/usr/bin/python3
"""
Overwrite print method
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):

    def test_e(self):
          r1 = Rectangle(4, 6, 2, 1, 12)
          self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')

    def test_eq(self):
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 5/5')

    def test_equ(self):
        r3 = Rectangle(5, 5, 1)
        self.assertEqual(str(r3), '[Rectangle] (2) 1/0 - 5/5')

    def test_equa(self):
        r4 = Rectangle(5, 5)
        self.assertEqual(str(r4), '[Rectangle] (3) 0/0 - 5/5')

    def test_equal(self):
        with self.assertRaises(TypeError) as cm:
            r4 = Rectangle(5)
        self.assertEqual("__init__() missing 1 required positional argument: 'height'", str(cm.exception))

    def test_equali(self):
        with self.assertRaises(TypeError) as cm:
            r5 = Rectangle()
        self.assertEqual("__init__() missing 2 required positional arguments: 'width' and 'height'", str(cm.exception))
