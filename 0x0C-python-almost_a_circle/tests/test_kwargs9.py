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

        r1.update(height=2, width=3)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 3/2")

        r1.update(height=2, y=1, width=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/1 - 2/2")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/3 - 4/2")

        r1.update(x=1, height=2, y=3, width=4, id=98)
        self.assertEqual(str(r1), "[Rectangle] (98) 1/3 - 4/2")

#        with self.assertRaises(KeyError) as cm:
#           r1.update(chicken=0)
#      self.assertEqual(str(cm.exception), "")

        with self.assertRaises(TypeError) as cm:
            r1.update(width='f')
        self.assertEqual(str(cm.exception), "width must be an integer")

        r1.update(2, 2, id=9)
        self.assertEqual(str(r1), "[Rectangle] (2) 1/3 - 2/2")

        r1.update(y=3, lol=666, width=89)
        self.assertEqual(str(r1), "[Rectangle] (2) 1/3 - 89/2")
