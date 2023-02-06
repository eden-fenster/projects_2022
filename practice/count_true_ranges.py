#!/usr/bin/env python3
from typing import List


def cnt_tru_rng_wrapper(mat: List[List[bool]]) -> int:
    return cnt_tru_rng(mat=mat, row=0, col=0, count=0)


def cnt_tru_rng(mat: List[List[bool]], row: int, col: int, count: int) -> int:
    # If we are out of range, return count.
    if row == len(mat):
        return count
    # If row ended, go to next one.
    if col == len(mat):
        return cnt_tru_rng(mat=mat, row=row + 1, col=0, count=count)
    # If we are at True, increment.
    if mat[row][col]:
        count += 1
        disable(mat=mat, row=row, col=col)
    # Move down the search path.
    return cnt_tru_rng(mat=mat, row=row, col=col + 1, count=count)


def is_legal(mat: List[List[bool]], row: int, col: int) -> bool:
    return 0 <= row <= len(mat) - 1 and 0 <= col <= len(mat) - 1


def disable(mat: List[List[bool]], row: int, col: int) -> None:
    if not is_legal(mat=mat, row=row, col=col) or not mat[row][col]:
        return
    mat[row][col] = False
    disable(mat=mat, row=row, col=col - 1)
    disable(mat=mat, row=row, col=col + 1)
    disable(mat=mat, row=row - 1, col=col)
    disable(mat=mat, row=row + 1, col=col)


def test_tru_cnt_rng():
    mat: List[List[bool]] = [[False, False, False, False, True],
                             [False, True, True, True, False],
                             [False, False, True, True, False],
                             [True, False, False, False, False],
                             [True, True, False, False, False]]
    assert cnt_tru_rng_wrapper(mat=mat) == 3
