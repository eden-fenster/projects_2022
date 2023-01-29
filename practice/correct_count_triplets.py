#!/usr/bin/env python3
from typing import List


def count_triplets_wrapper(array_of_numbers: List[int], num: int) -> int:
    return count_triplets(array_of_numbers=array_of_numbers, num=num, first_location=0,
                          second_location=1, third_location=2, number_of_correct_equations=0)


def count_triplets(array_of_numbers: List[int], num: int, first_location: int, second_location: int,
                   third_location: int, number_of_correct_equations: int) -> int:
    # print(f'First -> {first_location}, Second -> {second_location}, Third -> {third_location}')
    # If success, return # of correct equations.
    if array_of_numbers[first_location] == num:
        return number_of_correct_equations
    if first_location > len(array_of_numbers) - 3:
        return number_of_correct_equations
    # If second # reached the end or second # == num,
    # increment first #, change other #'s accordingly and continue down the search path.
    if second_location > len(array_of_numbers) - 2 or second_location + 1 == third_location:
        new_first_number_location: int = first_location + 1
        new_second_number_location: int = new_first_number_location + 1
        new_third_number_location: int = new_second_number_location + 1
        return count_triplets(array_of_numbers=array_of_numbers, num=num,
                              first_location=new_first_number_location,
                              second_location=new_second_number_location,
                              third_location=new_third_number_location,
                              number_of_correct_equations=number_of_correct_equations)
    # If third # reached the end or third # == num,
    # increment second #, change third # accordingly and continue down the search path.
    if third_location > len(array_of_numbers) - 1 or array_of_numbers[third_location] == num:
        new_second_number_location: int = second_location + 1
        new_third_number_location: int = new_second_number_location + 1
        return count_triplets(array_of_numbers=array_of_numbers, num=num,
                              first_location=first_location,
                              second_location=new_second_number_location,
                              third_location=new_third_number_location,
                              number_of_correct_equations=number_of_correct_equations)
    # if the three are >= num, increment second #, change third # accordingly and continue down the search path.
    if array_of_numbers[first_location] + array_of_numbers[second_location] + array_of_numbers[third_location] >= num:
        new_second_number_location: int = second_location + 1
        new_third_number_location: int = new_second_number_location + 1
        return count_triplets(array_of_numbers=array_of_numbers, num=num,
                              first_location=first_location,
                              second_location=new_second_number_location,
                              third_location=new_third_number_location,
                              number_of_correct_equations=number_of_correct_equations)

    # Else, the three are < num and continue down the search path while incrementing # of correct equations.
    return count_triplets(array_of_numbers=array_of_numbers, num=num, first_location=first_location,
                          second_location=second_location, third_location=third_location + 1,
                          number_of_correct_equations=number_of_correct_equations + 1)


def test_count_triplets():
    array: List[int] = [1, 3, 4, 5, 7]
    second_array: List[int] = [-2, 0, 1, 3]
    assert count_triplets_wrapper(array_of_numbers=second_array, num=2) == 2
    assert count_triplets_wrapper(array_of_numbers=array, num=12) == 4
