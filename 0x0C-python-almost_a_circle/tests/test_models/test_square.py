#!/usr/bin/python3
"""
build square class
"""
from models.square import Square
from models.rectangle import Rectangle
import unittest
import io
from contextlib import redirect_stdout

class TestBaseClass(unittest.TestCase):
#  10
    def test_e(self):
         s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        self.assertEqual(f.getvalue(), "#####\n#####\n#####\n#####\n#####\n")

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        f = io.StringIO()
        with redirect_stdout(f):
            s2.display()
        self.assertEqual(f.getvalue(), "  ##\n  ##\n")

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        f = io.StringIO()
        with redirect_stdout(f):
            s3.display()
        self.assertEqual(f.getvalue(), "\n\n\n ###\n ###\n ###\n")

        self.assertEqual(issubclass(Square, Rectangle), True)

#  #11
        def test_eq(self):
            s1 = Square(5)
            self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
            self.assertEqual(str(s1.size), "5")
            s1.size = 10
            self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
            self.assertEqual(s1.size, s1.width)
            self.assertEqual(s1.size, s1.height)

#  #12
        def test_equ(self):
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

#  #13
        def equa(self):
             r1 = Rectangle(10, 2, 1, 9)
             r1_dictionary = r1.to_dictionary()
             self.assertEqual(isinstance(r1_dictionary, dict), True)
             self.assertEqual(str(r1_dictionary), "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}")
             self.assertEqual(str(type(r1_dictionary)), "<class 'dict'>")
             r2 = Rectangle(1, 1)
             r2.update(**r1_dictionary)
             self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
             self.assertEqual(str(r1 == r2), "False")

#  #14
        def equal(self):
            s1 = Square(10, 2, 1)
            s1_dictionary = s1.to_dictionary()
            self.assertEqual(str(s1_dictionary), "{'id': 1, 'x': 2, 'size': 10, 'y': 1}")
            self.assertEqual((type(s1_dictionary)), "<class 'dict'>")
            s2 = Square(1, 1)
            s2.update(**s1_dictionary)
            self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
            self.assertEqual(s1 == s2, "False")
