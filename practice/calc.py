#!/usr/bin/env python3
import sys


def calc_wrapper(num: int, result: int, max_op: int) -> int:
    return calc(num=num, result=result, max_op=max_op,
                num_of_calculations=0, result_up_to_this_point=num, history_of_calculations='')


def calc(num: int, result: int, max_op: int, num_of_calculations: int,
         result_up_to_this_point: int, history_of_calculations: str) -> int:
    # If success, return history + # of calculations.
    if result_up_to_this_point == result:
        print(string_history(num=num, history_of_calculations=history_of_calculations,
                             num_of_calculations=num_of_calculations, num_in_history=0))
        return num_of_calculations
    # If failure, return 0.
    if num_of_calculations == max_op:
        return 0
    # Else, go over the 4 operations.
    add: int = calc(num=num, result=result, max_op=max_op, num_of_calculations=num_of_calculations + 1,
                    result_up_to_this_point=result_up_to_this_point + num,
                    history_of_calculations=history_of_calculations + "+")
    subtract: int = calc(num=num, result=result, max_op=max_op, num_of_calculations=num_of_calculations + 1,
                         result_up_to_this_point=result_up_to_this_point - num,
                         history_of_calculations=history_of_calculations + "-")
    multiply: int = calc(num=num, result=result, max_op=max_op, num_of_calculations=num_of_calculations + 1,
                         result_up_to_this_point=result_up_to_this_point * num,
                         history_of_calculations=history_of_calculations + "*")
    divide: int = calc(num=num, result=result, max_op=max_op, num_of_calculations=num_of_calculations + 1,
                       result_up_to_this_point=result_up_to_this_point // num,
                       history_of_calculations=history_of_calculations + "/")
    # Return the one with the smallest # of calculations that is legal.
    current_min: int = sys.maxsize
    if add != 0:
        current_min = add
    if subtract != 0:
        current_min = min(current_min, subtract)
    if multiply != 0:
        current_min = min(current_min, multiply)
    if divide != 0:
        current_min = min(current_min, divide)

    if current_min == sys.maxsize:
        return 0

    return current_min


def string_history(num: int, history_of_calculations: str, num_of_calculations: int, num_in_history: int) -> str:
    if num_in_history == num_of_calculations - 1:
        return str(num)
    return str(num) + \
           history_of_calculations[num_in_history] + \
           string_history(num=num, history_of_calculations=history_of_calculations,
                          num_of_calculations=num_of_calculations, num_in_history=num_in_history + 1)


def test_calc():
    assert calc_wrapper(num=1, result=3, max_op=4) == 2
