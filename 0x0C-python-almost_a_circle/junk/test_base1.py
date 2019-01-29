#!/usr/bin/python3
"""
Unittest for base class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_e(self):
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
