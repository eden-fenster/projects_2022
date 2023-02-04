#!/usr/bin/env python3
from typing import List


def is_sum_wrapper(list_of_numbers: List[int], num: int) -> bool:
    return is_sum(list_of_numbers=list_of_numbers,
                  location=0, num=num, first=0, second=0, third=0, added_num=0, counter=0)


def is_sum(list_of_numbers: List[int],
           location: int, num: int, first: int, second: int, third: int, added_num: int, counter: int) -> bool:
    # If location > len, return False.
    if location > len(list_of_numbers) - 1:
        return False
    # If three adjacent numbers, return False.
    if counter == 3 and first + 1 == second and second + 1 == third:
        return False
    # If num == 0, return True.
    if num == 0:
        return True
    # If two #'s
    if counter == 2:
        return is_sum(list_of_numbers=list_of_numbers, location=location + 1, num=num,
                      first=first, second=second, third=third, added_num=added_num, counter=counter) or \
               is_sum(list_of_numbers=list_of_numbers, location=location + 1, num=num - list_of_numbers[location],
                      first=first, second=second, third=location,
                      added_num=list_of_numbers[location], counter=counter + 1)
    # If one #
    if counter == 1:
        return is_sum(list_of_numbers=list_of_numbers, location=location + 1, num=num,
                      first=first, second=second, third=third, added_num=added_num, counter=counter) or \
               is_sum(list_of_numbers=list_of_numbers, location=location + 1, num=num - list_of_numbers[location],
                      first=first, second=location, third=third,
                      added_num=list_of_numbers[location], counter=counter + 1)
    # If none
    return is_sum(list_of_numbers=list_of_numbers, location=location + 1, num=num,
                  first=first, second=second, third=third, added_num=added_num, counter=counter) or \
           is_sum(list_of_numbers=list_of_numbers, location=location + 1, num=num - list_of_numbers[location],
                  first=location, second=second, third=third, added_num=list_of_numbers[location], counter=counter + 1)


def test_is_sum():
    lis: List[int] = [5, 4, 2, 1, 3]
    assert is_sum_wrapper(list_of_numbers=lis, num=0) is True
    assert is_sum_wrapper(list_of_numbers=lis, num=8) is True
    assert is_sum_wrapper(list_of_numbers=lis, num=9) is True
    assert is_sum_wrapper(list_of_numbers=lis, num=2) is True
    assert is_sum_wrapper(list_of_numbers=lis, num=11) is False
    assert is_sum_wrapper(list_of_numbers=lis, num=17) is False
