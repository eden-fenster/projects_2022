#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-07-06
Purpose: Random Snack Generator
"""

import argparse


# --------------------------------------------------
from typing import List

from methods.add_snacks import Snacks as Snacks
from methods.choose_random_snack import Choose as Choose


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
    snack_list: List[str] = Snacks.add_snacks(snacks=snacks)
    print(Choose.choose_random_snack(snack_list))


if __name__ == '__main__':
    main()
