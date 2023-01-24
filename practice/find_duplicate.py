#!/usr/bin/env python3
from typing import List


def find_duplicate(list_of_numbers: List[int]) -> int:
    # Sorting list in ascending order.
    list_of_numbers.sort()
    # Looping over sorted array.
    for number in range(0, len(list_of_numbers) - 1):
        # If success, return number.
        if list_of_numbers[number] == list_of_numbers[number + 1]:
            return list_of_numbers[number]
        # Else, continue down the search path.
        continue
    # If failure, return -1.
    return -1


def test_find_duplicate():
    first_list: List[int] = [2, 4, 5, 3, 5, 1]
    second_list: List[int] = [1, 1, 1, 2, 2, 2, 2]
    assert find_duplicate(list_of_numbers=first_list) == 5
    assert find_duplicate(list_of_numbers=second_list) == 1
