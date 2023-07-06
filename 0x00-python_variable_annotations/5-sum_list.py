#!/usr/bin/env python3
""" A type-annotated sum_list function """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A type-annotated function return sum of floats from a list.
    """
    return sum(input_list)
