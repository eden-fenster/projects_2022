#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class ComparisonResults:
    correct_locations: int
    correct_numbers: int
    had_error: bool


def compare_numbers(correct_number: str, guessed_number: str, number_of_digits: int) -> ComparisonResults:
    cr = ComparisonResults(correct_locations=0, correct_numbers=0, had_error=False)
    for i in range(0, number_of_digits):
        guessed_digit = guessed_number[i]
        if not guessed_digit.isdigit():
            cr.had_error = True
            break
        if correct_number[i] == guessed_digit:
            cr.correct_locations += 1
            continue
        if guessed_digit in correct_number:
            cr.correct_numbers += 1
            continue
    return cr
