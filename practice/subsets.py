#!/usr/bin/env python3
from typing import List


def subset_wrapper(original_array: List[int], target_sum: int) -> List[int]:
    possible_solutions: List[int] = []
    return subset(original_array=original_array, current_index=0,
                  target_sum=target_sum, possible_solution=possible_solutions, prefix='')


def subset(original_array: List[int], current_index: int,
           target_sum: int, possible_solution: List[int], prefix: str) -> List[int]:
    print(f"{prefix}Called with {current_index=}, {target_sum=}, {possible_solution=}")
    # Stopping conditions
    # On success we return a list of numbers.
    # k =0 - success
    if target_sum == 0:
        return possible_solution
    # On failure, we return an empty list
    # End of array - failure
    if current_index > len(original_array)-1:
        print(f"{prefix}Reached end of array")
        return []
    # target_sum < 0 - failure.
    if target_sum < 0:
        return []
    # We proceed with/without current element and see if there is a success
    without_current_element: List[int] = subset(original_array=original_array, current_index=current_index + 1,
                                                target_sum=target_sum,
                                                possible_solution=possible_solution, prefix=prefix+"   ")
    if without_current_element:
        return without_current_element

    value = original_array[current_index]
    new_possible_solution = list(possible_solution)
    new_possible_solution.append(value)
    with_current_element: List[int] = subset(original_array=original_array, current_index=current_index + 1,
                                             target_sum=target_sum - value,
                                             possible_solution=new_possible_solution, prefix=prefix+"   ")
    if with_current_element:
        return with_current_element
    return []


def test_subset():
    """Test"""
    array: List[int] = [1, 2, 4, 5]
    k: int = 7
    print(subset_wrapper(array, k))
    print(subset_wrapper(array, 9))
    print(subset_wrapper(array, 0))
    print(subset_wrapper(array, 3))
