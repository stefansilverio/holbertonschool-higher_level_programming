#!/usr/bin/python3
"""
Unittest for rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):

    def test_e(self):
        r0 = Rectangle(2, 5)
        self.assertEqual(issubclass(Rectangle, Base), True)
        r1 = Rectangle(10, 2, 4, 6)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 2)
        with self.assertRaises(TypeError) as cm:
            r2 = Rectangle()
        self.assertEqual("__init__() missing 2 required positional \
arguments: 'width' and 'height'", str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r3 = Rectangle(10)
        self.assertEqual("__init__() missing 1 required positional \
argument: 'height'", str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r4 = Rectangle(1, 1, 1, 1, 1, 1)
        self.assertEqual("__init__() takes from 3 to 6 positional \
arguments but 7 were given", str(cm.exception))
        r5 = Rectangle(2, 10)
        self.assertEqual(r5.width, 2)
        self.assertEqual(r5.height, 10)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)
        self.assertEqual(r5.id, 3)
        r6 = Rectangle(3, 12, 3)
        self.assertEqual(r6.width, 3)
        self.assertEqual(r6.height, 12)
        self.assertEqual(r6.x, 3)
        self.assertEqual(r6.y, 0)
        self.assertEqual(r6.id, 4)
        r7 = Rectangle(6, 6, 6, 6)
        self.assertEqual(r7.width, 6)
        self.assertEqual(r7.height, 6)
        self.assertEqual(r7.x, 6)
        self.assertEqual(r7.y, 6)
        self.assertEqual(r7.id, 5)
        r8 = Rectangle(10, 7, 0, 5, "almond")
        self.assertEqual(r8.width, 10)
        self.assertEqual(r8.height, 7)
        self.assertEqual(r8.x, 0)
        self.assertEqual(r8.y, 5)
        self.assertEqual(r8.id, "almond")
