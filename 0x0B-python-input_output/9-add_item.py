#!/usr/bin/python3
import sys
import json
import os.path
"""
add args to pylist
Return:
none
"""


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

exists = os.path.isfile("add_item.json")

if exists:
    lista = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        lista.append(sys.argv[i])
    save_to_json_file(lista, "add_item.json")
else:
    l = []
    for i in range(1, len(sys.argv)):
        l.append(sys.argv[i])
    save_to_json_file(l, "add_item.json")
