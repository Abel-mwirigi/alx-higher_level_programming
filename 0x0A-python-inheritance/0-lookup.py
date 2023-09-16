#!/usr/bin/python3
"""function that returns the list of available attributes and methods"""


def lookup(obj):
    """
    Returns a list of methods and attributes
    Args:
    obj:object to inspect
    Returns:
    a list: list of attributes
    """
    return dir(obj)
