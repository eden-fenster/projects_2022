#!/usr/bin/env python3
# Gets from user a 9 x 9 board.
from typing import List


def is_soduku_wrapper(soduku: List[List[int]]) -> bool:
    return is_soduku(soduku, 0, 0, 1, 1)


def is_soduku(soduku: List[List[int]], where_in_row: int, where_in_col: int, range_of_row: int,
              range_of_col: int) -> bool:
    # Checks to see if it's a soduku , if not - fail.
    # if rows don't have 1 - 9, fail.
    if not is_list_part_of_soduku(row=soduku[where_in_row]):
        return False
    if not is_list_part_of_soduku(row=soduku[where_in_row[where_in_col]]):
        return False
    # # If a range of i (0-2, 3-5, 6-8) and j (0-2, 3-5, 6-8) is missing numbers between 1 - 9, fail.
    # If all pass, win.
    return True

# Checks to see if row is part of soduku.
def is_list_part_of_soduku(row: List[int]) -> bool:
    # If length is not 9, fail.
    if len(row) != 9:
        return False
    # If 1 - 9 do not all appear, fail.
    if 1 not in row or 2 not in row or 3 not in row or 4 not in row or 5 not in row or 6 not in row or 7 not in row \
            or 8 not in row or 9 not in row:
        return False
    # else, win and move to next row.
    return True
# Checks to see if range is part of soduku.
def is_range_part_of_soduku(soduku: List[List[int]], range_of_row: int, range_of_col: int) -> bool:
    pass