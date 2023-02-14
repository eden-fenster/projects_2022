#!/usr/bin/env python3

def same_pattern_wrapper(first_string: str, second_string: str) -> bool:
    return same_pattern(first_string=first_string, pattern_string=second_string,
                        location_in_first=0, location_in_pattern=0, pattern_from_string='')


def same_pattern(first_string: str, pattern_string: str,
                 location_in_first: int, location_in_pattern: int, pattern_from_string: str) -> bool:
    # print(f'Pattern -> {pattern_from_string}')
    # If second string is just an *, return true.
    if pattern_string is '*':
        return True
    # If both are the same, return true.
    if first_string is pattern_string:
        return True
    # If pattern from second not in first, return False.
    if pattern_from_string not in first_string:
        return False
    # If we reached the end of the second string, return True.
    if location_in_pattern >= len(pattern_string):
        return True
    # If we reached the end of the first string, return true.
    if location_in_first >= len(first_string):
        return False
    # If we reached an *, the pattern that we are looking for is reset.
    if pattern_string[location_in_pattern] is '*':
        return same_pattern(first_string=first_string, pattern_string=pattern_string,
                            location_in_first=location_in_first,
                            location_in_pattern=location_in_pattern + 1, pattern_from_string='') \
               or same_pattern(first_string=first_string, pattern_string=pattern_string,
                               location_in_first=location_in_first + 1, location_in_pattern=location_in_pattern,
                               pattern_from_string=pattern_from_string)
    # Else, continue.
    return same_pattern(first_string=first_string, pattern_string=pattern_string,
                        location_in_first=location_in_first + 1,
                        location_in_pattern=location_in_pattern + 1,
                        pattern_from_string=pattern_from_string + pattern_string[location_in_pattern])


def test_same_pattern():
    first_string: str = "TheExamIsEasy"
    assert same_pattern_wrapper(first_string=first_string, second_string="The*xamIs*y") is True
    assert same_pattern_wrapper(first_string=first_string, second_string="The*mIsEasy*") is True
    assert same_pattern_wrapper(first_string=first_string, second_string="*") is True
    assert same_pattern_wrapper(first_string=first_string, second_string="TheExamIsEasy") is True
    assert same_pattern_wrapper(first_string=first_string, second_string="The*IsHard") is False
