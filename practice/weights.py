#!/usr/bin/env python3
from typing import List


def weights_sum_wrapper(a: List[int], sum_of_weights: int) -> bool:
    return weights_sum(a, 0, len(a) - 1, sum_of_weights)


def weights_sum(a: List[int], i: int, j: int, sum_of_weights: int) -> bool:
    if i >= len(a) - 1 or j <= 0:
        return False

    if a[i] + a[j] == sum_of_weights or a[i] == sum_of_weights or a[j] == sum_of_weights:
        return True

    return \
        weights_sum(a=a, i=i + 1, j=j, sum_of_weights=sum_of_weights) and \
        weights_sum(a=a, i=i, j=j - 1, sum_of_weights=sum_of_weights) or \
        (weights_sum(a=a, i=i + 1, j=j, sum_of_weights=sum_of_weights) or
         weights_sum(a=a, i=i, j=j - 1, sum_of_weights=sum_of_weights))


def test_weights():
    """Test method"""
    array: List[int] = [1, 7, 9, 3]
    weight_sum: int = 12
    example = weights_sum_wrapper(a=array, sum_of_weights=weight_sum)
    assert example is True
    weight_sum_two: int = 15
    example_two = weights_sum_wrapper(a=array, sum_of_weights=weight_sum_two)
    assert example_two is False
