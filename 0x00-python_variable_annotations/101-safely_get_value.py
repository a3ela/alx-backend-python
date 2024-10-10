#!/usr/bin/env python3
from typing import Any, Mapping, TypeVar

T = TypeVar('T')  # Define a type variable


def safely_get_value(dct: Mapping[str, T], key: str, default: T = None) -> T:
    '''safely_get_value safely retrieves a value from a dictionary.

    Args:
        dct (Mapping[str, T]): The dictionary to retrieve the value from.
        key (str): The key to look for in the dictionary.
        default (T, optional): The default value to return \
            if the key is not found. Defaults to None.

    Returns:
        T: The value associated with the given key if it exists, \
            otherwise the default value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
