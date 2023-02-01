#!/usr/bin/env python3


def my_compare_wrapper(first_string: str, second_string: str) -> int:
    return my_compare(first_string=first_string, second_string=second_string, location_in_first=0,
                      location_in_second=0)


def my_compare(first_string: str, second_string: str, location_in_first: int, location_in_second: int) -> int:
    # If first < second and first is done, return -1.
    if location_in_first == len(first_string) and location_in_second < len(second_string):
        return -1
    # If first > second and second is done, return 1.
    if location_in_second == len(second_string) and location_in_first < len(first_string):
        return 1
    # If the sane, return 0.
    if first_string is second_string:
        return 0
    # If letter in first < letter in second
    if first_string[location_in_first] < second_string[location_in_second]:
        return -1
    # If letter in first > letter in second
    if first_string[location_in_first] > second_string[location_in_second]:
        return 1

    # If two letters are equal, continue down the search path.
    return my_compare(first_string=first_string, second_string=second_string, location_in_first=location_in_first + 1,
                      location_in_second=location_in_second + 1)


def test_my_compare():
    assert my_compare_wrapper(first_string="mother", second_string="hello") == 1
    assert my_compare_wrapper(first_string="hell", second_string="hello") == -1

