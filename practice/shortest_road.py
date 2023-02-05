#!/usr/bin/env python3
from typing import List


def shortest_road_wrapper(first: List[int], second: List[int]) -> int:
    return min(shortest_road(first=first, second=second, location=0, switched=False, starting_at=1, sum_min=0),
               shortest_road(first=first, second=second, location=0, switched=False, starting_at=2, sum_min=0))


def shortest_road(first: List[int],
                  second: List[int], location: int, switched: bool, starting_at: int, sum_min: int) -> int:
    # If end is reached, return sum of minutes.
    if location == len(first):
        return sum_min
    # If we already switched, move one way.
    if switched:
        if starting_at == 2:
            return shortest_road(first=first, second=second, location=location + 1, switched=switched,
                                 starting_at=starting_at, sum_min=sum_min + first[location])

        return shortest_road(first=first, second=second, location=location + 1, switched=switched,
                             starting_at=starting_at, sum_min=sum_min + second[location])
    # Else, move both ways and return max value.
    if starting_at == 2:
        return min(shortest_road(first=first, second=second, location=location + 1, switched=switched,
                                 starting_at=starting_at, sum_min=sum_min + second[location]),
                   shortest_road(first=first, second=second, location=location + 1, switched=True,
                                 starting_at=starting_at, sum_min=sum_min + second[location]))
    return min(shortest_road(first=first, second=second, location=location + 1, switched=switched,
                             starting_at=starting_at, sum_min=sum_min + first[location]),
               shortest_road(first=first, second=second, location=location + 1, switched=True,
                             starting_at=starting_at, sum_min=sum_min + first[location]))


def test_shortest_road():
    road_one: List[int] = [5, 4, 5, 8, 12, 9, 9, 3]
    road_two: List[int] = [7, 3, 3, 12, 10, 2, 10, 7]
    assert shortest_road_wrapper(first=road_one, second=road_two) == 49
