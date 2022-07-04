#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-06-19
Purpose: Bul_Pgia
"""

# --------------------------------------------------
import argparse
from generate_number import generate_number as generator
from compare_numbers import compare_numbers as compare


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bul_Pgia',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-d',
                        '--num-digits',
                        help='Number of digits',
                        metavar='Number of digits',
                        type=int,
                        default=4)

    parser.add_argument('-t',
                        '--num-tries',
                        help='Number of tries',
                        metavar='Number of tries',
                        type=int,
                        default=3)

    parser.add_argument('-r',
                        '--repeat-digits',
                        help='Repeat digits',
                        type=bool,
                        default=False)

    args = parser.parse_args()

    if args.num_digits < 1:
        parser.error(f'--num-digits "{args.num_digits}" must be bigger than 0')

    return args


def main() -> None:
    args = get_args()
    number_of_digits: int = args.num_digits
    number_of_tries: int = args.num_tries
    duplicate_digits_allowed: bool = args.repeat_digits
    # Setup:
    # Generate a random number with K digits and optionally allowing for digits to be repeated.
    number = generator(number_of_digits=number_of_digits, can_repeat_digits=duplicate_digits_allowed)
    tries_so_far: int = 0

    while True:
        # The user is asked to input a guess of what the number is.
        guessed_number = input("Input your guess  \n")
        # Calculate how many digits match in place, how many match out of place, how many totally wrong.
        comparison_results = compare(correct_number=number, guessed_number=guessed_number,
                                                     number_of_digits=number_of_digits)
        if comparison_results.had_error:
            print("Had error, re enter")
            continue

        # if all digits match – you won.
        if comparison_results.correct_locations == number_of_digits:
            print('You won !')
            break

        # Otherwise print counters.
        print(f'correct locations - {comparison_results.correct_locations}')
        print(f'correct numbers - {comparison_results.correct_numbers}')

        tries_so_far += 1

        # If you didn’t guess after N  (parameter) times, you lose, and we exit the program.
        if tries_so_far >= number_of_tries:
            print(f'You lose, loser.\nthe number was {number}')
            break


def test_compare_numbers():
    cr = compare('1234', '123a', 4)
    assert cr.had_error is True
    cr = compare('22234', '43322', 5)
    assert cr.correct_numbers == 5


def test_generate_number():
    assert generator(2, False) == '12'


if __name__ == '__main__':
    main()
