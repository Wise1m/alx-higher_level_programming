#!/usr/bin/python3
"""Defines an function that adds two integers."""


def add_integer(a, b=98):
    """Returns the addition of a and b.

    Floats are converted to int before addition is performed.

    Raises:
        TypeError; if either of a or b is a non-integer and non-float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
