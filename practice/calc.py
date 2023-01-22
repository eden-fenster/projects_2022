#!/usr/bin/env python3
def calc_wrapper(num: int, result: int, max_op: int) -> int:
    return calc(num=num, result=result, max_op=max_op,
                num_of_calculations=0, result_up_to_this_point=0, history_of_calculations='')


def calc(num: int, result: int, max_op: int, num_of_calculations: int,
         result_up_to_this_point: int, history_of_calculations: str) -> int:
    # If success, return history + add to counter of right solutions.
    if result_up_to_this_point == result:
        # print(string_history(num=num, history_of_calculations=history_of_calculations,
        # num_of_calculations=num_of_calculations, num_in_history=0))
        return 1
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
    # Return the sum of # of legal right solutions.
    return add + subtract + multiply + divide


def string_history(num: int, history_of_calculations: str, num_of_calculations: int, num_in_history: int) -> str:
    if num_in_history == num_of_calculations - 1:
        return str(num)
    return str(num) + \
        history_of_calculations[num_in_history] + \
        string_history(num=num, history_of_calculations=history_of_calculations,
                       num_of_calculations=num_of_calculations, num_in_history=num_in_history)


def test_calc():
    assert calc_wrapper(3, 36, 4) == 3
