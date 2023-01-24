#!/usr/bin/env python3
from typing import List


def k_almost_search(almost_sorted_list: List[int], num: int) -> int:
    # Looping over the list.
    for number in range(0, len(almost_sorted_list)):
        # If success, return index of number in List.
        if almost_sorted_list[number] == num:
            return number
        if almost_sorted_list[number] < num:
            continue
        # If failure, return -1
        if almost_sorted_list[number] > num:
            return -1



def test_k_almost_search():
    almost_sorted_list: List[int] = [3, 0, 0, 4, 7, 9, 0, 0, 0, 0, 11, 15, 0, 19, 20, 0, 0, 31, 40, 0]
    assert k_almost_search(almost_sorted_list=almost_sorted_list, num=9) == 5
    assert k_almost_search(almost_sorted_list=almost_sorted_list, num=31) == 17
    assert k_almost_search(almost_sorted_list=almost_sorted_list, num=30) == -1
