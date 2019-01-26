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

    def test_eq(self):
        b2 = Base()
        self.assertEqual(2, b2.id)

    def test_equ(self):
        b3 = Base()
        self.assertEqual(3, b3.id)

    def test_equa(self):
        b4 = Base(12)
        self.assertEqual(12, b4.id)

    def test_equal(self):
        b5 = Base()
        self.assertEqual(4, b5.id)

if __name__ == '__main__':
    unittest.main()
