#!/usr/bin/python3
"""
module 7-add_item
"""

from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_name = "add_item.json"

try:
    persistent = load_from_json_file(file_name)
except FileNotFoundError:
    persistent = []

save_to_json_file(persistent + argv[1:], file_name)
