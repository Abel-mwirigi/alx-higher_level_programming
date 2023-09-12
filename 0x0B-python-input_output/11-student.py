#!/usr/bin/pyhton3
"""A Student Class"""


class Student:
    """A Student blueprint"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representationof a Student instance
        Args:
                attrs: is a list of strings, only attribute names contained in this
                list must be retrieved otherwise all attributes must be retrieved"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except FileNotFoundError:
                pass
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
