#!/usr/bin/env python3
from typing import List


def cross_sort_wrapper(list_of_numbers: List[int]) -> List[int]:
    return cross_sort(list_of_numbers=list_of_numbers, first_location=0, second_location=1)


def cross_sort(list_of_numbers: List[int], first_location: int, second_location: int) -> List[int]:
    # If we reached the end, return sorted list.
    if first_location == len(list_of_numbers) - 1:
        return list_of_numbers
    # If we did all possible swaps with first_location,
    # move down the search path and increment first_location by 1 and second_location accordingly.
    if second_location == len(list_of_numbers):
        new_first_location: int = first_location + 1
        return cross_sort(list_of_numbers=list_of_numbers, first_location=new_first_location,
                          second_location=new_first_location + 1)
    # If number at second < number at first, swap.
    if list_of_numbers[second_location] < list_of_numbers[first_location]:
        temp: int = list_of_numbers[second_location]
        list_of_numbers[second_location] = list_of_numbers[first_location]
        list_of_numbers[first_location] = temp
    # Move down the search path and increment second by 1.
    return cross_sort(list_of_numbers=list_of_numbers, first_location=first_location,
                      second_location=second_location + 1)


def test_cross_sort():
    lis: List[int] = [1, 9, 2, 8, 4, 7, 7, 4, 12]
    assert cross_sort_wrapper(list_of_numbers=lis) == [1, 2, 4, 4, 7, 7, 8, 9, 12]
