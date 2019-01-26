#!/usr/bin/python3
"""
build square class
"""
import unittest
import io
from contextlib import redirect_stdout
from models.square import Square

class TestBaseClass(unittest.TestCase):
    def test_e(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        self.assertEqual(f.getvalue(), "#####\n#####\n#####\n#####\n#####\n")

        print("---")

    def test_eq(self):
        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        f = io.StringIO()
        with redirect_stdout(f):
            s2.display()
        self.assertEqual(f.getvalue(), "  ##\n  ##\n")

        print("---")

    def test_equ(self):
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        f = io.StringIO()
        with redirect_stdout(f):
            s3.display()
        self.assertEqual(f.getvalue(), "\n\n\n ###\n ###\n ###\n")
