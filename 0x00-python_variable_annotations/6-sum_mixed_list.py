#!/usr/bin/env python3
'''module for sum_mixed_list'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns the sum of the list of floats and ints'''
    return sum(mxd_lst)
