#!/usr/bin/env python3
from typing import List

marked: int = -1


def print_path_weights_wrapper(paths: List[List[int]]) -> int:
    return print_path_weights(paths=paths, row=0, col=0, sum_of_path=paths[0][0])


def print_path_weights(paths: List[List[int]], row: int, col: int, sum_of_path: int) -> int:
    print(f'Value -> {paths[row][col]} \n Row -> {row} \n Col -> {col}')
    # If we were already here, return path
    if paths[row][col] == marked:
        return sum_of_path
    # If out of range, return 0
    if row < 0 or col < 0:
        return 0
    if row > len(paths) - 1 or col > len(paths[0]) - 1:
        return 0
    # If we reached the end, return sum of path
    if row == len(paths) - 1 and col == len(paths[row]) - 1:
        return sum_of_path
    # We mark our spot and move down the search path.
    paths[row][col] = marked
    north: int = print_path_weights(paths=paths, row=row - 1, col=col, sum_of_path=sum_of_path + paths[row - 1][col])
    south: int = print_path_weights(paths=paths, row=row + 1, col=col, sum_of_path=sum_of_path + paths[row + 1][col])
    east: int = print_path_weights(paths=paths, row=row, col=col + 1, sum_of_path=sum_of_path + paths[row][col + 1])
    west: int = print_path_weights(paths=paths, row=row, col=col - 1, sum_of_path=sum_of_path + paths[row][col - 1])
    # Return the largest sum of the paths
    return max(north, south, east, west)


def test_print_path_weights():
    lis: List[List[int]] = [[1, 2], [3, 4]]
    assert print_path_weights_wrapper(paths=lis) == 8
