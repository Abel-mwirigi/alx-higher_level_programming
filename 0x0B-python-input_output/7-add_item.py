#!/usr/bin/python3
"""
Add all arguments to python list and save them to a file
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
try:
    list_members = load_from_json_file(file)
except FileNotFoundError:
    list_members = []

for arg in argv[1:]:
    list_members.append(arg)

save_to_json_file(list_members, file)
