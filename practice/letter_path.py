#!/usr/bin/env python3
from typing import List


def length_path_wrapper(mat: List[List[str]], pattern: str) -> int:
    return length_path(mat=mat, row=0, col=0, pattern=pattern, length_of_path=0)


def length_path(mat: List[List[str]], row: int, col: int, pattern: str, length_of_path: int) -> int:
    # If failure, return length of path.
    if mat[row][col] not in pattern \
            or row < 0 or col < 0 or row > len(mat) - 1 or col > len(mat[0]) - 1 or mat[row][col] == -1:
        return length_of_path

    # Mark current position and move down search path.
    mat[row][col] = str(-1)
    north: int = length_path(mat=mat, row=row - 1, col=col, pattern=pattern, length_of_path=length_of_path + 1)
    south: int = length_path(mat=mat, row=row + 1, col=col, pattern=pattern, length_of_path=length_of_path + 1)
    east: int = length_path(mat=mat, row=row, col=col + 1, pattern=pattern, length_of_path=length_of_path + 1)
    west: int = length_path(mat=mat, row=row, col=col - 1, pattern=pattern, length_of_path=length_of_path + 1)

    # Finding and returning the biggest result, if result bigger than 0, success.
    return max(north, south, east, west)


def max_path_wrapper(mat: List[List[str]], pattern: str) -> int:
    return max_path(mat=mat, row=0, col=0, pattern=pattern)


def max_path(mat: List[List[str]], row: int, col: int, pattern: str) -> int:
    # If illegal coordinates, failure and return 0.
    if row < 0 or col < 0 or row > len(mat) - 1 or col > len(mat[0]) - 1:
        return 0
    # Calculating path starting from[row][col]
    path: int = length_path(mat=mat, row=row, col=col, pattern=pattern, length_of_path=0)
    # Moving down the search path and calculating path with a starting point at every position.
    north: int = max_path(mat=mat, row=row - 1, col=col, pattern=pattern)
    south: int = max_path(mat=mat, row=row + 1, col=col, pattern=pattern)
    east: int = max_path(mat=mat, row=row, col=col + 1, pattern=pattern)
    west: int = max_path(mat=mat, row=row, col=col - 1, pattern=pattern)
    # If max > 0, success.
    return max(path, north, south, east, west)


def test_length_path_and_max_path():
    first_list: List[List[str]] = [['a', 'c', 'b', 'c', '@', 'a'], ['b', 'x', 'z', 'c', 's', 'a'],
                                   ['?', 'c', 'd', '*', 'c', 'd'], ['b', 'c', 'a', '8', 'b', 'b'],
                                   ['c', '2', 'x', '+', 'b', 'c']]
    second_list: List[List[str]] = [['a', 'd', 'e', 's', '@', 'a'], ['3', 'a', 'z', 'a', 's', 'a'],
                                    ['?', 'c', 'b', 'b', 'c', 'd'], ['b', 'c', 'a', '8', 'b', 'b'],
                                    ['c', '2', 'x', '+', 'b', 'c']]

    assert length_path_wrapper(mat=first_list, pattern='abc') == 5
    assert max_path_wrapper(mat=second_list, pattern='abc') == 11
