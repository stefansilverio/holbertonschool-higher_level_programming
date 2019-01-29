#!/usr/bin/python3
"""Unittest for rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout


class TestBaseClass(unittest.TestCase):
    def test_inher(self):
        #  #2
        r0 = Rectangle(2, 5)
        self.assertEqual(issubclass(Rectangle, Base), True)
        r1 = Rectangle(10, 2, 4, 6)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 2)
        with self.assertRaises(TypeError) as cm:
            r2 = Rectangle()
        self.assertEqual("__init__() missing 2 required positional \
arguments: 'width' and 'height'", str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r3 = Rectangle(10)
        self.assertEqual("__init__() missing 1 required positional \
argument: 'height'", str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r4 = Rectangle(1, 1, 1, 1, 1, 1)
        self.assertEqual("__init__() takes from 3 to 6 positional \
arguments but 7 were given", str(cm.exception))
        r5 = Rectangle(2, 10)
        self.assertEqual(r5.width, 2)
        self.assertEqual(r5.height, 10)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)
        self.assertEqual(r5.id, 3)
        r6 = Rectangle(3, 12, 3)
        self.assertEqual(r6.width, 3)
        self.assertEqual(r6.height, 12)
        self.assertEqual(r6.x, 3)
        self.assertEqual(r6.y, 0)
        self.assertEqual(r6.id, 4)
        r7 = Rectangle(6, 6, 6, 6)
        self.assertEqual(r7.width, 6)
        self.assertEqual(r7.height, 6)
        self.assertEqual(r7.x, 6)
        self.assertEqual(r7.y, 6)
        self.assertEqual(r7.id, 5)
        r8 = Rectangle(10, 7, 0, 5, "almond")
        self.assertEqual(r8.width, 10)
        self.assertEqual(r8.height, 7)
        self.assertEqual(r8.x, 0)
        self.assertEqual(r8.y, 5)
        self.assertEqual(r8.id, "almond")

#  #3
    def test_val(self):
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle("10", 2)
        self.assertEqual('width must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(10, "2")
        self.assertEqual('height must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(10, 2, "3", 2)
        self.assertEqual('x must be an integer', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(10, 2, 3, "2")
        self.assertEqual('y must be an integer', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(10, 2, -3, 2)
        self.assertEqual('x must be >= 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(10, 2, 3, -2)
        self.assertEqual('y must be >= 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(-10, 2, 3, 2)
        self.assertEqual('width must be > 0', str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(10, -2, 3, 2)
        self.assertEqual('height must be > 0', str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r2 = Rectangle()
        self.assertEqual("__init__() missing 2 required positional \
arguments: 'width' and 'height'", str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r2 = Rectangle(2)
        self.assertEqual("__init__() missing 1 required positional \
argument: 'height'", str(cm.exception))

#  #4
    def test_area(self):
        r1 = Rectangle(5, 5)
        self.assertEqual(r1.area(), 25)
        r2 = Rectangle(3, 2)
        self.assertEqual(r2.area(), 6)
        r3 = Rectangle(2, 10)
        self.assertEqual(r3.area(), 20)
        r4 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r4.area(), 56)
        with self.assertRaises(TypeError) as cm:
            r5 = Rectangle(4)
        self.assertEqual("__init__() missing 1 required positional argument: \
'height'", str(cm.exception))

#  #5
    def test_disp0(self):
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

#  #6
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 5/5')
        r3 = Rectangle(5, 5, 1)
        self.assertEqual(str(r3), '[Rectangle] (2) 1/0 - 5/5')
        r4 = Rectangle(5, 5)
        self.assertEqual(str(r4), '[Rectangle] (3) 0/0 - 5/5')
        with self.assertRaises(TypeError) as cm:
            r4 = Rectangle(5)
        self.assertEqual("__init__() missing 1 required positional \
argument: 'height'", str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            r5 = Rectangle()
        self.assertEqual("__init__() missing 2 required positional \
arguments: 'width' and 'height'", str(cm.exception))

#  #7
    def test_disp1(self):
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

#  #8
    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        r1 = Rectangle(80, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 80/2")
        r1.update(50, 20)
        self.assertEqual(str(r1), "[Rectangle] (50) 3/4 - 20/2")
        with self.assertRaises(TypeError) as cm:
            r1.update(1, "f")
        self.assertEqual(str(cm.exception), "width must be an integer")
        with self.assertRaises(TypeError) as cm:
            r1.update()
        self.assertEqual(str(cm.exception), "missing 2 required positional \
arguments: 'width' and 'height'")

#  #9
    def test_update2(self):
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
        with self.assertRaises(TypeError) as cm:
            r1.update(width='f')
        self.assertEqual(str(cm.exception), "width must be an integer")
        r1.update(2, 2, id=9)
        self.assertEqual(str(r1), "[Rectangle] (2) 1/3 - 2/2")
        r1.update(y=3, lol=666, width=89)
        self.assertEqual(str(r1), "[Rectangle] (2) 1/3 - 89/2")
