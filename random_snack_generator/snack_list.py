#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-02-06
Purpose: Random Snack Generator
"""

import argparse


# --------------------------------------------------
import random
from typing import List


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Random Snack Generator',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('snacks',
                        metavar='str',
                        nargs='+',
                        help='what snacks do we have for Noogi at the house')

    return parser.parse_args()


def main():
    args = get_args()
    snacks: str = args.snacks
    print(add_snacks(snacks=snacks))


def add_snacks(snacks: str) -> str:
    number_of_snacks: int = len(snacks)
    snacks_in_house: List[str] = []
    if number_of_snacks == 1:
        snacks_in_house.append(snacks[0])
    if number_of_snacks > 1:
        for snack in snacks:
            snacks_in_house.append(snack)
    return ' '.join(snacks_in_house)


def choose_random_snack(snacks: List[str]) -> str:
    return random.choice(snacks)

# --------------------------------------------------
if __name__ == '__main__':
    main()
