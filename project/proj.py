# project/proj.py

"""Provide several sample math calculations.
a delta

This module allows the user to make mathematical calculations.

Examples:
    >>> from project import proj
    >>> proj.add(2, 4)
    6.0
    >>> proj.multiply(2.0, 4.0)
    8.0
    >>> from project.proj import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

from typing import Union


def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a (float): A number representing the first addend in the addition.
        b (float): A number representing the second addend in the addition.

    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)


def subtract(a, b):
    return float(a - b)


def multiply(a, b):
    return float(a * b)


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
