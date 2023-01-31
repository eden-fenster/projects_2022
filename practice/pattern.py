#!/usr/bin/env python3

def same_pattern_wrapper(first_string: str, second_string: str) -> bool:
    return same_pattern(first_string=first_string, second_string=second_string,
                        location_in_second=0, pattern_from_second='')


def same_pattern(first_string: str, second_string: str, location_in_second: int, pattern_from_second: str) -> bool:
    # print(f'Pattern -> {pattern_from_second}')
    # If second string is just an *, return true.
    if second_string is '*':
        return True
    # If both are the same, return true.
    if first_string is second_string:
        return True
    # If pattern from second not in first, return False.
    if pattern_from_second not in first_string:
        return False
    # If we reached the end of the second string, return True.
    if location_in_second >= len(second_string):
        return True
    # If we reached an *, the pattern that we are looking for is reset.
    if second_string[location_in_second] is '*':
        return same_pattern(first_string=first_string, second_string=second_string,
                            location_in_second=location_in_second + 1, pattern_from_second='')
    # Else, continue.
    return same_pattern(first_string=first_string, second_string=second_string,
                        location_in_second=location_in_second + 1,
                        pattern_from_second=pattern_from_second + second_string[location_in_second])


def test_same_pattern():
    first_string: str = "TheExamIsEasy"
    assert same_pattern_wrapper(first_string=first_string, second_string="The*xamIs*y") is True
    assert same_pattern_wrapper(first_string=first_string, second_string="The*mIsEasy*") is True
    assert same_pattern_wrapper(first_string=first_string, second_string="*") is True
    assert same_pattern_wrapper(first_string=first_string, second_string="TheExamIsEasy") is True
    assert same_pattern_wrapper(first_string=first_string, second_string="The*IsHard") is False
