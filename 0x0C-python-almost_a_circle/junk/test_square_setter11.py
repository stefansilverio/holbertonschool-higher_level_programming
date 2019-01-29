#!/usr/bin/python3
"""
Set square size
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):

    def test_e(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(s1.size), "5")
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, s1.width)
        self.assertEqual(s1.size, s1.height)
