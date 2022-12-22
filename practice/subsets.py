#!/usr/bin/env python3
from typing import List


def subset_wrapper(a: List[int], k: int) -> List[int]:
    new_array: List[int] = [] * len(a)
    return subset(a=a, i=0, j=0, k=k, new_array=new_array)


def subset(a: List[int], i: int, j: int, k: int, new_array: List[int]) -> List[int]:
    if i < len(a) - 1 and k > 0:
        without_subtraction: List[int] = subset(a=a, i=i + 1, j=j, k=k, new_array=new_array)
        value = a[i]
        new_array[j] = value
        with_subtraction: List[int] = subset(a=a, i=i + 1, j=j + 1, k=k - value, new_array=new_array)
        return without_subtraction or with_subtraction
    if k < 0 and i < len(a) - 1:
        value = new_array.pop()
        return subset(a=a, i=i + 1, j=j - 1, k=k + value, new_array=new_array)
    if k != 0 and i == len(a) - 1:
        return []
    if k == 0 and i == 0:
        return [0]
    return new_array


def test_subset():
    """Test"""
    array: List[int] = [1, 2, 3, 4, 5]
    k: int = 7
    assert subset_wrapper(array, k) == [1, 2, 4]
