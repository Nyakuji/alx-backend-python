#!/usr/bin/env python3
""" Complex types -string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple where the first element is the string k
    and the second element is the square of the int/float v
    (annotated as float).

    Parameters:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple containing string k and the square
        of v (as a float).
    """
    return (k, v * v)
