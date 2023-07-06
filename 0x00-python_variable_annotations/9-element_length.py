#!/usr/bin/env python3
""" Typing: Iterable, sequence and Tuple """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A type-annotated function returning list of tuples of int numbers.
    """
    return [(i, len(i)) for i in lst]
