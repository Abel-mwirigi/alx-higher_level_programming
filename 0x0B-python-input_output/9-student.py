#!/usr/bin/python3
"""A Student class"""


class Student:
    """Student blueprint"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """producds dict representation of the student"""
        return self.__dict__
