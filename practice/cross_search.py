#!/usr/bin/env python3
from typing import List


def cross_search_wrapper(list_of_numbers: List[int], num: int) -> int:
    return cross_search(list_of_numbers=list_of_numbers, num=num, location_in_list=0)


def cross_search(list_of_numbers: List[int], num: int, location_in_list: int) -> int:
    # If we reached the end without finding num, return -1.
    if location_in_list == len(list_of_numbers):
        return -1
    # If num found, return index.
    if list_of_numbers[location_in_list] == num:
        return location_in_list
    # Else, continue down the search path.
    return cross_search(list_of_numbers=list_of_numbers, num=num, location_in_list=location_in_list + 1)


def test_cross_search():
    lis: List[int] = [1, 9, 2, 8, 4, 7, 7, 4, 12]
    assert cross_search_wrapper(list_of_numbers=lis, num=4) == 4
    assert cross_search_wrapper(list_of_numbers=lis, num=11) == -1
