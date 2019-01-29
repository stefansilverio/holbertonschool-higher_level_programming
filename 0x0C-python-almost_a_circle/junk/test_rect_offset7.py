#!/usr/bin/python3
"""
Consider offset
"""
import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    def test_e(self):
        r1 = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        r2 = Rectangle(3, 2, 1, 0)
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), " ###\n ###\n")

        r3 = Rectangle(5, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r3.display()
        self.assertEqual(f.getvalue(), "#####\n#####\n")
