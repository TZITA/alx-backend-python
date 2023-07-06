#!/usr/bin/env python3
""" A type-annotated to_kv function """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A type-annotated function that returns a tuple.
    """
    return (k, v*v)
