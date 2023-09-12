#!/usr/bin/python3
"""This is python class to JSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a data structure"""
    return obj.__dict__
