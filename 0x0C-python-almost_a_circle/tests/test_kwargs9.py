#!/usr/bin.python3
"""
Unittest for kwargs
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):

    def test_e(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_eq(self):
        r2 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r2), "[Rectangle] (2) 10/10 - 10/10")

        r2.update(x=0)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/10 - 10/10")
