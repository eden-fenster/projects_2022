#!/usr/bin/env python3
from typing import List


def subset_wrapper(a: List[int], k: int) -> List[int]:
    new_array: List[int] = []
    return subset(a=a, i=0, j=0, k=k, new_array=new_array)


def subset(a: List[int], i: int, j: int, k: int, new_array: List[int]) -> List[int]:
    if i >= len(a) - 1 or k == 0:
        return new_array
    if k < 0 and i < len(a) - 1:
        value = new_array.pop()
        return subset(a=a, i=i + 1, j=j - 1, k=k + value, new_array=new_array)
    if k == 0 and i == 0:
        return [0]
    print(f'currently on {a[i]}')
    without_subtraction: List[int] = subset(a=a, i=i + 1, j=j, k=k, new_array=new_array)
    value = a[i]
    print(f'{value} is being added to new_array')
    with_subtraction: List[int] = subset(a=a, i=i + 1, j=j + 1, k=k - value, new_array=new_array)
    new_array.append(value)
    return without_subtraction or with_subtraction



def test_subset():
    """Test"""
    array: List[int] = [1, 2, 3, 4, 5]
    k: int = 7
    assert subset_wrapper(array, k) == [1, 2, 4]
