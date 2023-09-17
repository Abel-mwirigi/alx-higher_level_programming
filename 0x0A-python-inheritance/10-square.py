#!/usr/bin/python3
"""Inheritance via importing the class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle which
    inherits from BaseGeometry
    """

    def __init__(self, size):
        """Initializing a new object of a square"""
        self.integer_validator("size", size)
        """using the inherited methods"""
        super().__init__(size, size)
        """By performing a super it means for this class
        alter the way it is initalized from width, height to size, size"""
        self.__size = size
