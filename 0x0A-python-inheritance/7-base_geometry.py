#!/usr/bin/python3
"""
Defining a baseGeometry class
"""


class BaseGeometry:
    """
    creating an baseGeometry class
    """

    def area(self):
        """
        to be implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the values of integers

        Args:
        name (str): A string representing the name of the value being validated.
        value (int): The value to validate.

        Raises:
        TypeError: If 'value' is not an integer.
        ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
