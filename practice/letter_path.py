#!/usr/bin/env python3
from typing import List

marker: str = '-1'


def length_path_wrapper(mat: List[List[str]], pattern: str) -> int:
    return length_path(mat=mat, row=0, col=0, pattern=pattern, length_of_path=0)


def length_path(mat: List[List[str]], row: int, col: int, pattern: str, length_of_path: int) -> int:
    # If failure, return length of path.
    if row < 0 or col < 0:
        return length_of_path
    if row > len(mat) - 1 or col > len(mat[row]) - 1:
        return length_of_path
    if mat[row][col] == marker:
        return length_of_path
    if mat[row][col] not in pattern:
        return length_of_path

    # Mark current position and move down search path.
    mat[row][col] = marker
    north: int = length_path(mat=mat, row=row - 1, col=col,
                             pattern=pattern, length_of_path=length_of_path + 1)
    south: int = length_path(mat=mat, row=row + 1, col=col,
                             pattern=pattern, length_of_path=length_of_path + 1)
    east: int = length_path(mat=mat, row=row, col=col + 1,
                            pattern=pattern, length_of_path=length_of_path + 1)
    west: int = length_path(mat=mat, row=row, col=col - 1,
                            pattern=pattern, length_of_path=length_of_path + 1)

    # Finding and returning the biggest result, if result bigger than 0, success.
    return max(north, south, east, west)


def max_path_wrapper(mat: List[List[str]], pattern: str) -> int:
    return max_path(mat=mat, row=0, col=0, pattern=pattern, max_length_found=0)


def max_path(mat: List[List[str]], row: int, col: int, pattern: str, max_length_found: int) -> int:
    # If done, return length.
    if row > len(mat) - 1:
        return max_length_found
    # If row is done, move to next one.
    if col > len(mat[row]) - 1:
        return max_path(mat=mat, row=row + 1, col=0, pattern=pattern, max_length_found=max_length_found)
    # Starting path from current position.
    path: int = length_path(mat=mat, row=row, col=col, pattern=pattern, length_of_path=0)
    # If path > max, change max
    max_length_found = max(max_length_found, path)
    # Moving down the search path
    return max_path(mat=mat, row=row, col=col + 1, pattern=pattern, max_length_found=max_length_found)


def test_length_path_and_max_path():
    first_list: List[List[str]] = [['a', 'c', 'b', 'c', '@', 'a'], ['b', 'x', 'z', 'c', 's', 'a'],
                                   ['?', 'c', 'd', '*', 'c', 'd'], ['b', 'c', 'a', '8', 'b', 'b'],
                                   ['c', '2', 'x', '+', 'b', 'c']]
    second_list: List[List[str]] = [['a', 'd', 'e', 's', '@', 'a'], ['3', 'a', 'z', 'a', 's', 'a'],
                                    ['?', 'c', 'b', 'b', 'c', 'd'], ['b', 'c', 'a', '8', 'b', 'b'],
                                    ['c', '2', 'x', '+', 'b', 'c']]

    assert length_path_wrapper(mat=first_list, pattern='abc') == 5
    assert max_path_wrapper(mat=second_list, pattern='abc') == 11
