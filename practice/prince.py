#!/usr/bin/env python3
import sys
from typing import List

BAD_GUY_MARKER: int = -1
MARK_PLACE: int = -2
FIRST_PLACEHOLDER_VALUE: int = -3
NEED_TO_BACKTRACK: int = -1
MAX_GO_UP: int = 1
MAX_GO_DOWN: int = 2


def prince_wrapper(drm: List[int][int], i: int, j: int) -> int:
    drm_clone: List[int][int] = drm.copy()
    return prince(drm_clone, i, j, FIRST_PLACEHOLDER_VALUE, 0)


def prince(drm: List[int][int], i: int, j: int, previous_location_value: int, counter: int) -> int:
    if (i >= len(drm)) or (j >= len(drm)) or (i < 0) or (j < 0):
        return NEED_TO_BACKTRACK

    if drm[i][j] == BAD_GUY_MARKER:
        # print("Bad guy found with a length of " + (counter + 1) + " in (" + i + "," + j + ")")
        return counter + 1

    our_value: int = drm[i][j]
    if our_value == MARK_PLACE:
        return NEED_TO_BACKTRACK

    if previous_location_value != FIRST_PLACEHOLDER_VALUE:
        difference = (our_value - previous_location_value)
        if (difference > MAX_GO_UP) or (difference < -1 * MAX_GO_DOWN):
            return NEED_TO_BACKTRACK

    drm[i][j] = MARK_PLACE
    #  print("Taking (" + i + "," + j + ")")

    min_left: int = prince(drm, i - 1, j, our_value, counter + 1)
    min_right: int = prince(drm, i + 1, j, our_value, counter + 1)
    min_up: int = prince(drm, i, j - 1, our_value, counter + 1)
    min_down: int = prince(drm, i, j + 1, our_value, counter + 1)

    current_min: int = sys.maxsize

    if min_left != -1:
        current_min = min_left
    if min_right != -1:
        current_min = min(min_right, current_min)
    if min_up != -1:
        current_min = min(current_min, min_up)
    if min_down != -1:
        current_min = min(current_min, min_down)

    if current_min == sys.maxsize:
        # print("Back tracking from (" + i + "," + j + ")")
        return NEED_TO_BACKTRACK
    return current_min
