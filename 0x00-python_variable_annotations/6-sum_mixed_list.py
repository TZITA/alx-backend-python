#!/usr/bin/env python3
""" A type-annotated sum_mixed_list function """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A type-annotated function that returns sum of int and floats from a list.
    """
    return sum(mxd_lst)
