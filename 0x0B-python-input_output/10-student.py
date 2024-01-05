#!/usr/bin/python3
"""Defines a class Student."""


class Student():
    """A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes ths Student class.
         Args:
            first_name(str),
            last_name(str),
            age(int).
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
