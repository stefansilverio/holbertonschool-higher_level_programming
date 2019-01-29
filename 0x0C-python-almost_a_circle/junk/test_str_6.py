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
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 5/5')
        r3 = Rectangle(5, 5, 1)
        self.assertEqual(str(r3), '[Rectangle] (2) 1/0 - 5/5')
        r4 = Rectangle(5, 5)
        self.assertEqual(str(r4), '[Rectangle] (3) 0/0 - 5/5')
        with self.assertRaises(TypeError) as cm:
            r4 = Rectangle(5)
        self.assertEqual("__init__() missing 1 required positional \
argument: 'height'", str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r5 = Rectangle()
        self.assertEqual("__init__() missing 2 required positional \
arguments: 'width' and 'height'", str(cm.exception))
