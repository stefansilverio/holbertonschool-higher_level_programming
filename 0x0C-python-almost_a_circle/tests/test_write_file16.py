#!/usr/bin/python3
"""write json str to file"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    def test_e(self):
         r1 = Rectangle(10, 7, 2, 8)
         r2 = Rectangle(2, 4)
         Rectangle.save_to_file([r1, r2])

         with open("Rectangle.json", "r") as file:
             self.assertEqual(file.read(), str([{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]))
