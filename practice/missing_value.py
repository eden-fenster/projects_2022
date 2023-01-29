#!/usr/bin/env python3
from typing import List


def missing_value(sorted_list: List[int]) -> int:
    diff: int = 0
    # Looping over the list.
    for location in range(0, len(sorted_list) - 2):
        # If diff between the soon is the same, continue.
        if sorted_list[location + 1] - sorted_list[location] == sorted_list[location + 2] - sorted_list[location + 1]:
            diff = sorted_list[location + 1] - sorted_list[location]
            continue
        # Else, return number -> smaller number in diff equation + regular diff.
        if location == 0:
            return sorted_list[location] + diff
        return sorted_list[location + 1] + diff


def test_missing_value():
    sorted_list: List[int] = [7, 10, 13, 16, 22, 25]
    assert missing_value(sorted_list=sorted_list) == 19
