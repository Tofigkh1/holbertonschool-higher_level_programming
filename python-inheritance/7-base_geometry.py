#!/usr/bin/python3
"""BaseGeometry module."""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Raise an exception for unimplemented method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.
        
        Args:
            name (str): The name of the variable.
            value (int): The value to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
