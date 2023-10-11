#!/usr/bin/python3
"""Module 9-student
Creates a student file
"""


class Student:
    """Defines a student
    Public sttributes:
        - first_name
        - last_name
        - age
    Public method to_json()
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the student instances"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a student instance
        Returns: the dict representation of the instance
        """

        return self.__dict__
