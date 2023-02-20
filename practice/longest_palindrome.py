#!/usr/bin/env python3
from typing import List


def longest_palindrome_wrapper(list_of_numbers: List[int]):
    return longest_palindrome(list_of_numbers=list_of_numbers, location_one=0, location_two=len(list_of_numbers) - 1)


def longest_palindrome(list_of_numbers: List[int], location_one: int, location_two):
    # If out of range, return 0.
    if location_one == len(list_of_numbers) or location_two == len(list_of_numbers):
        return 0
    # If palindrome, return length.
    if is_palindrome(list_of_numbers=list_of_numbers, location_one=location_one, location_two=location_two):
        return location_two - location_one + 1
    # Else, move down the search path.
    return max(longest_palindrome(list_of_numbers=list_of_numbers,
                                  location_one=location_one + 1, location_two=location_two),
               longest_palindrome(list_of_numbers=list_of_numbers, location_one=location_one + 1,
                                  location_two=location_two - 1),
               longest_palindrome(list_of_numbers=list_of_numbers, location_one=location_one,
                                  location_two=location_two - 1))


def is_palindrome(list_of_numbers: List[int], location_one: int, location_two: int) -> bool:
    # If at middle, true.
    if location_one == location_two or location_two < location_one:
        return True
    # If not equal, false.
    if list_of_numbers[location_one] != list_of_numbers[location_two]:
        return False
    # Move down the search path.
    return is_palindrome(list_of_numbers=list_of_numbers, location_one=location_one + 1,
                         location_two=location_two - 1)


def test_longest_palindrome():
    list_to_do: List[int] = [1, 3, 2, 3, 10, 10, 3, 2, 4]
    assert longest_palindrome_wrapper(list_of_numbers=list_to_do) == 6