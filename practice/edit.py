#!/usr/bin/env python3


def edit_wrapper(first_string: str, second_string: str) -> int:
    return edit(first_string=first_string, second_string=second_string, first_location=0, second_location=0,
                number_of_changes=0)


def edit(first_string: str, second_string: str, first_location: int,
         second_location: int, number_of_changes: int) -> int:
    print(f'First -> {first_string}, Second -> {second_string}')
    # If success, return number of changes.
    if first_string == second_string:
        return number_of_changes
    # if first[i] not second[j] and first < second, don't omit first[i] and move down the search path.
    if first_string[first_location] is not second_string[second_location] and len(first_string) < len(second_string):
        first_string = first_string[:first_location] + second_string[first_location] + first_string[first_location:]
        return edit(first_string=first_string, second_string=second_string, first_location=first_location + 1,
                    second_location=second_location + 1, number_of_changes=number_of_changes + 1)
    # if first[i] not second[j] and first >= second, omit first[i] and move down the search path.
    if first_string[first_location] is not second_string[second_location] and len(first_string) >= len(second_string):
        first_string = first_string[:first_location] + second_string[first_location] + first_string[first_location + 1:]
        return edit(first_string=first_string, second_string=second_string, first_location=first_location + 1,
                    second_location=second_location + 1, number_of_changes=number_of_changes + 1)
    # Else, move down the search path without making changes.
    return edit(first_string=first_string, second_string=second_string, first_location=first_location + 1,
                second_location=second_location + 1, number_of_changes=number_of_changes)


def test_edit():
    assert edit_wrapper(first_string='geek', second_string='gesek') == 1
    assert edit_wrapper(first_string='sunday', second_string='saturday') == 3
