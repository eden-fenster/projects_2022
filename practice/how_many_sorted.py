#!/usr/bin/env python3

def how_many_sorted_wrapper(length: int, max_num: int) -> int:
    return how_many_sorted(length=length, max_num=max_num, location=0, current_num=1)


def how_many_sorted(length: int, max_num: int, location: int, current_num: int) -> int:
    # If length == max, return # of options.
    if length == max_num:
        return (length * max_num) - 1
    # If at end, return.
    if location == length:
        return 0
    if current_num > max_num:
        return 0
    # Moving down the search path.
    if location == 0:
        return 1 + how_many_sorted(length=length, max_num=max_num,
                                   location=location + 1, current_num=current_num + 1) + \
               how_many_sorted(length=length, max_num=max_num,
                               location=location, current_num=current_num + 1)
    return 1 + how_many_sorted(length=length, max_num=max_num,
                               location=location + 1, current_num=current_num + 1) + \
           how_many_sorted(length=length, max_num=max_num,
                           location=location + 1, current_num=current_num) + \
           how_many_sorted(length=length, max_num=max_num,
                           location=location, current_num=current_num + 1)


def test_how_many_sorted():
    assert how_many_sorted_wrapper(length=3, max_num=2) == 4
    assert how_many_sorted_wrapper(length=2, max_num=3) == 6
    assert how_many_sorted_wrapper(length=3, max_num=3) == 8
    assert how_many_sorted_wrapper(length=2, max_num=4) == 10
