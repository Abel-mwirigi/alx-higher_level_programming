#!/usr/bin/python3
"""this module implemets inheritance via importing the class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This Rectangle class is inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initializing a new recatangle with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
