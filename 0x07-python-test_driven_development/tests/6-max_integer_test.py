#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_compare(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_empty(self):
        self.assertEqual(max_integer([None]), None)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        self.assertEqual(max_integer([4]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, 4]), 4)

    def test_str(self):
        self.assertEqual(max_integer(["stef", "cat", "is"]), "stef")

    def test_two(self):
        self.assertEqual(max_integer("stef"), "t")


if __name__ == '__main__':
    unittest.main()
