#!/usr/bin/env python3
from typing import List

from range import Range


def find_num_wrapper(ranges: List[Range], num: int) -> int:
    return find_num(ranges=ranges, num=num, location=0)


def find_num(ranges: List[Range], num: int, location: int) -> int:
    # If end is reached without number being found, -1.
    if location == len(ranges):
        return -1
    # If center +/- radius = num or - < num < + ,return index.
    add: int = ranges[location].get_center() + ranges[location].get_radius()
    subtract: int = ranges[location].get_center() - ranges[location].get_radius()
    if add == num:
        return location
    if subtract == num:
        return location
    if subtract < num < add:
        return location
    # Else, move down the search path.
    return find_num(ranges=ranges, num=num, location=location + 1)


def test_find_num():
    ranges: List[Range] = [Range(4, 1), Range(12, 0), Range(20, 1), Range(102, 2)]
    assert find_num_wrapper(ranges=ranges, num=5) == 0
    assert find_num_wrapper(ranges=ranges, num=101) == 3
    assert find_num_wrapper(ranges=ranges, num=15) == -1
    assert find_num_wrapper(ranges=ranges, num=105) == -1
