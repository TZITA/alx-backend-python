#!/usr/bin/env python3
""" A type-annotated function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function that returns a function.
    """
    def mult(fl: float) -> float:
        """ Multiplies a float by multiplier """
        return fl * multiplier
    return mult
