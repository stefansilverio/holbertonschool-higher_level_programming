#!/usr/bin/python3
"""
Unittest for rectangle setters
"""
import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):

    def test_e(self):
        r1 = Rectangle(4, 6)
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "####\n####\n####\n####\n####\n####\n")

        r2 = Rectangle(2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

        with self.assertRaises(TypeError) as cm:
            r3 = Rectangle(2)
        self.assertEqual("__init__() missing 1 required \
positional argument: 'height'", str(cm.exception))
