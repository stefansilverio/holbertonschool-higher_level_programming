#!/usr/bin/python3
"""
return instance with all attributes set
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    def test_e(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r1)
        print(r2)
        print(r1 is r2)
        print(r1 == r2)
