#!/usr/bin/env python3
'''module for element_length'''
from typing import Sequence, List, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns a list of tuples containing elements and their lengths'''
    return [(i, len(i)) for i in lst]
