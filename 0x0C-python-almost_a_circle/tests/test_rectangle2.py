#!/usr/bin/python3
"""
Unittest for rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):

    def test_e(self):
         r1 = Rectangle(10, 2)
         self.assertEqual(r1.id, 1)

    def test_eq(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def test_equ(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_equa(self):
        r4 = Rectangle(10, 2, 4, 0, 12)
        self.assertEqual(r4.x, 4)

    def test_equal(self):
        r5 = Rectangle(10, 2, 0, 15, 12)
        self.assertEqual(r5.y, 15)

    def test_equals(self):
        r6 = Rectangle(10, 7, 0, 5, 12)
        self.assertEqual(r6.width, 10)

    def test_equals(self):
        r7 = Rectangle(10, 7, 0, 5, 12)
        self.assertEqual(r7.height, 7)

if __name__ == '__main__':
    unittest.main()
