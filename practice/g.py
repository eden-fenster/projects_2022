#!/usr/bin/env python3
from typing import List


def g_wrapper(list_of_numbers: List[int]) -> List[int]:
    return g(list_of_numbers=list_of_numbers, location=0)


def s(list_of_numbers: List[int], counter: int, location: int) -> int:
    if counter == location:
        return list_of_numbers[counter]
    # print(f'number -> {list_of_numbers[counter]}')
    return list_of_numbers[counter] + s(list_of_numbers=list_of_numbers, counter=counter + 1, location=location)


def g(list_of_numbers: List[int], location: int) -> List[int]:
    # If we reached the end, return.
    if location == len(list_of_numbers):
        return list_of_numbers
    # If sum of 0 - location < 0, change from negative to positive.
    if s(list_of_numbers=list_of_numbers, counter=0, location=location) < 0:
        # print(f'Number before change -> {list_of_numbers[location]}')
        list_of_numbers[location] = list_of_numbers[location] * -1
        # print(f'Number after change -> {list_of_numbers[location]}')
    return g(list_of_numbers=list_of_numbers, location=location + 1)


def test_g():
    lis: List[int] = [1, 2, -4, 8]
    assert g_wrapper(list_of_numbers=lis) == [1, 2, 4, 8]
