#!/usr/bin/python3
'''module for safe_first_element'''
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''returns the first element of a list if it exists'''
    if lst:
        return lst[0]
    else:
        return None
