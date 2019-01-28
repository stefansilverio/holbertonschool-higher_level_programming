#!/usr/bin/python3
"""
Unittest for rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):

    def test_e(self):
        r1 = Rectangle(5, 5)
        self.assertEqual(r1.area(), 25)
        r2 = Rectangle(3, 2)
        self.assertEqual(r2.area(), 6)
        r3 = Rectangle(2, 10)
        self.assertEqual(r3.area(), 20)
        r4 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r4.area(), 56)
        with self.assertRaises(TypeError) as cm:
            r5 = Rectangle(4)
        self.assertEqual("__init__() missing 1 required positional argument: \
'height'", str(cm.exception))
