#!/usr/bin/python3
"""return json string list"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    def test_e(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(str("[{}] {}".format(type(list_input), list_input)), "[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]")
        self.assertEqual(str("[{}] {}".format(type(json_list_input), json_list_input)), "[<class 'str'>]" '[{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]')
        self.assertEqual(str("[{}] {}".format(type(list_output), list_output)), "[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]")
