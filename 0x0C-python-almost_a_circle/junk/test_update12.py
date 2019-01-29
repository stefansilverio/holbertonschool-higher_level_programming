#!/usr/bin/python3
"""
update square size
"""
import unittest
from models.base import Base
from models.square import Square


class TestBaseClass(unittest.TestCase):
    def test_e(self):
            s1 = Square(5)
            self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
            s1.update(10)
            self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
            s1.update(1, 2)
            self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
            s1.update(1, 2, 3)
            self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
            s1.update(1, 2, 3, 4)
            self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
            s1.update(x=12)
            self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
            s1.update(size=7, y=1)
            self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
            s1.update(size=7, id=89, y=1)
            self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")
            s1.update("cat")
            self.assertEqual(str(s1), "[Square] (cat) 12/1 - 7")
            with self.assertRaises(TypeError) as cm:
                s1.update(10, "f")
            self.assertEqual(str(cm.exception), "width must be an integer")
