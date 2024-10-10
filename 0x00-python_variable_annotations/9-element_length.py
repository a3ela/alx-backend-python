#!/usr/bin/env python3
'''module for element_length'''
from typing import Sequence, List, Iterable


def element_length(lst: Iterable[Squence[int]]) -> List[int]:
    '''returns a list of tuples containing elements and their lengths'''
    return [(i, len(i)) for i in lst]
