#!/usr/bin/env python3
""" A type-annotated sum_list function """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A type-annotated function return sum of floats from a list.
    """
    sum = 0
    for i in range(len(input_list)):
        sum += input_list[i]
    return sum
