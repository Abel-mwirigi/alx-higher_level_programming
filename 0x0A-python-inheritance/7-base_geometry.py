#!/usr/bin/python3
"""
Defining a baseGeometry class
"""


class BaseGeometry:
    """creating an baseGeometry class"""

    def area(self):
        """to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the values of integers"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
