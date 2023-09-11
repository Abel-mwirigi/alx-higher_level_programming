#!/usr/bin/python3
"""Inheritance via importing the class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle which inherits from BaseGeometry"""

    def __init__(self, size):
        """Initializing a new object of a square"""
        super().__init__(size, size)
        ### self.integer_validator("size", size)###
        """By performing a super it means for this class alter
        the way it is initalized from width, height to size, size"""
        self.__size = size

    def __str__(self):
        """returns the print() and str() representation of a square"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
