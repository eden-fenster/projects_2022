#!/usr/bin/env python3
from typing import List


def missing_value(sorted_list: int) -> int:
    diff: int = 0
    # Looping over the list.
    for location in range(0, sorted_list - 2):
        # If diff between the soon is the same, continue.
        if sorted_list[location + 1] - sorted_list[location] == sorted_list[location + 2] - sorted_list[location + 1]:
            diff = sorted_list[location + 1] - sorted_list[location]
            continue
        # Else, return number -> smaller number in diff equation + regular diff.
        return sorted_list[location + 1] + diff
