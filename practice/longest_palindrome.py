#!/usr/bin/env python3
from typing import List


def longest_palindrome_wrapper(list_of_numbers: List[int]):
    return longest_palindrome(list_of_numbers=list_of_numbers, location=0, current=0, longest=0)


def longest_palindrome(list_of_numbers: List[int], location: int, current: int, longest: int):
    # If out of range, return length of current palindrome.
    if location < 0 or location >= len(list_of_numbers):
        return current
    # If current > longest.
    if current > longest:
        longest = current
    
    left: int = \
        longest_palindrome(list_of_numbers=list_of_numbers, location=location - 1, current=current + 1, longest=longest)
    right: int = \
        longest_palindrome(list_of_numbers=list_of_numbers, location=location + 1, current=current + 1, longest=longest)
