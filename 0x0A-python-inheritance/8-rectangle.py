#!/usr/bin/python3
"""Module Rectangle
Creates a Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle
    Private instance attributes:
        - width
        - height
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes an instance

        Args:
            - width: rectangle width
            - height: rectangle height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
