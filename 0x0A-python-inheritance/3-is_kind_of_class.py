#!/usr/bin/python3
"""Checks if an object is an instance fo a class"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns true if object is an instance of that class
    or if it inherits from that class"""

    return isinstance(obj, a_class)
