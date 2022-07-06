#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-07-06
Purpose: Random Snack Generator
"""

import argparse


# --------------------------------------------------
from typing import List

from add_snacks import add_snacks as add_snacks
from choose_random_snack import choose_random_snack as choose_random_snack


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
    snack_list: List[str] = add_snacks(snacks=snacks)
    print(choose_random_snack(snack_list))


if __name__ == '__main__':
    main()
