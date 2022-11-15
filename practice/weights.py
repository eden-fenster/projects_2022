#!/usr/bin/env python3
from typing import List


def weights_sum_wrapper(a: List[int], sum_of_weights: int) -> bool:
    return weights_sum(a, 0, sum_of_weights, False)


def weights_sum(a: List[int], i: int, sum_of_weights: int, taken: bool) -> bool:
    if i >= len(a) - 1:
        return False
    if sum_of_weights == 0:
        return True
    if sum_of_weights < 0:
        return False
    if weights_sum(a, i + 1, sum_of_weights, False):
        return True
    value: int = a[i]
    return weights_sum(a, i + 1, sum_of_weights - value, True)


def test_weights():
    """Test method"""
    array: List[int] = [1, 7, 9, 3]
    weight_sum: int = 12
    example = weights_sum_wrapper(a=array, sum_of_weights=weight_sum)
    assert example is True
    weight_sum_two: int = 15
    example_two = weights_sum_wrapper(a=array, sum_of_weights=weight_sum_two)
    assert example_two is False
