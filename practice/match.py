#!/usr/bin/env python3
from typing import List

two_digits_only: int = 2
one_digit_only: int = 1
either_one_or_two: int = 0


def match_wrapper(numbers: List[int], pattern: List[int]) -> bool:
    return match(numbers=numbers, pattern=pattern, location_in_numbers=0, location_in_pattern=0)


def match(numbers: List[int], pattern: List[int], location_in_numbers: int, location_in_pattern: int) -> bool:
    # If pattern is empty, true.
    if not pattern:
        return True
    # If numbers < pattern, false.
    if len(numbers) < len(pattern):
        return False
    # If we reached the end of the pattern, true.
    if location_in_pattern == len(pattern):
        return True
    # If we have not found anything, false.
    if location_in_numbers == len(numbers):
        return False
    # If triple digit, move one number and reset pattern.
    if numbers[location_in_numbers] >= 100:
        return match(numbers=numbers, pattern=pattern,
                     location_in_numbers=location_in_numbers + 1, location_in_pattern=0)
    # If pattern is two digit only.
    if pattern[location_in_pattern] == two_digits_only:
        # If it's a single digit.
        if numbers[location_in_numbers] < 10:
            if location_in_numbers == len(numbers) - 1:
                return False
            return match(numbers=numbers, pattern=pattern,
                         location_in_numbers=location_in_numbers, location_in_pattern=0)
        # If end of pattern is reached, true.
        if location_in_pattern == len(pattern) - 1:
            return True
        return match(numbers=numbers, pattern=pattern, location_in_numbers=location_in_numbers + 1,
                     location_in_pattern=location_in_pattern + 1)
    # If pattern is one digit only.
    if pattern[location_in_pattern] == one_digit_only:
        # If it's a double digit.
        if 10 <= numbers[location_in_numbers] < 100:
            if location_in_numbers == len(numbers) - 1:
                return False
            return match(numbers=numbers, pattern=pattern,
                         location_in_numbers=location_in_numbers, location_in_pattern=0)
        # If end of pattern is reached, return true.
        if location_in_pattern == len(pattern) - 1:
            return True
        return match(numbers=numbers, pattern=pattern, location_in_numbers=location_in_numbers + 1,
                     location_in_pattern=location_in_pattern + 1)
    # If it's either type of digit.
    if location_in_pattern == len(pattern) - 1:
        return True
    return match(numbers=numbers, pattern=pattern, location_in_numbers=location_in_numbers + 1,
                 location_in_pattern=location_in_pattern + 1)


def test_match():
    pattern: List[int] = [1, 0, 2]
    assert match_wrapper(numbers=[2, 3, 57], pattern=pattern) is True
    assert match_wrapper(numbers=[5, 39, 67], pattern=pattern) is True
    assert match_wrapper(numbers=[2, 3, 573, 4, 34, 35], pattern=pattern) is True
    assert match_wrapper(numbers=[2, 3, 573, 4, 324, 35], pattern=[]) is True
    assert match_wrapper(numbers=[2, 3], pattern=pattern) is False
    assert match_wrapper(numbers=[2, 3, 573, 4, 324, 35], pattern=pattern) is False
