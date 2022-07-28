#!/usr/bin/env python3
import argparse
from typing import Tuple, List

from snack_list_database_sqlalchemy import FoodDatabase

food_list = FoodDatabase()


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Snack Generator',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--add_snack',
                        help='Add a snack',
                        dest='add_snack',
                        default=True,
                        action='store_true')

    parser.add_argument('-m',
                        '--add_many_snacks',
                        help='Add more than one snack',
                        dest='add_snack',
                        default=True,
                        action='store_false')

    parser.add_argument('-d',
                        '--delete_snack',
                        help='Delete a snack',
                        default=False,
                        action='store_true')

    parser.add_argument('-r',
                        '--random_snack',
                        help='Return a random snack',
                        dest='random_snack',
                        default=True,
                        action='store_true')

    parser.add_argument('-l',
                        '--lookup_snacks',
                        help='Search for snacks based on availability',
                        default=False,
                        action='store_true')

    parser.add_argument('-s',
                        '--show_all',
                        help='Return all snacks',
                        dest='random_snack',
                        default=True,
                        action='store_false')

    return parser.parse_args()


def main() -> None:
    args = get_args()
    add_snack: bool = args.add_snack
    delete_snack: bool = args.delete_snack
    lookup_snacks: bool = args.lookup_snacks
    random_snack: bool = args.random_snack

    if add_snack:
        snack_name: str = input('Input snack name.')
        snack_availability: str = input('Type True for yes and False for no.')
        food_list.add_one(snack_name, snack_availability)

    else:
        num: str = input('How many snack do you want to add ?')
        if not num.isdigit():
            num: str = input('Not a number, try again !')
        num_to_add: int = int(num)
        snacks_to_add: List[Tuple[str, str]] = []
        for i in range(0, num_to_add):
            snack_name: str = input('Input snack name.')
            snack_availability: str = input('Type True for yes and False for no.')
            snack: Tuple[str, str] = (snack_name, snack_availability)
            snacks_to_add.append(snack)
            food_list.add_many(snacks_to_add)

    if delete_snack:
        food_to_delete: str = input('What food do you want to delete ?')
        food_list.delete_one(food_to_delete)

    if lookup_snacks:
        condition: str = input('Type True for available and False for not available.')
        food_list.food_lookup_by_availability(condition)

    if random_snack:
        food_list.choose_random()
    else:
        food_list.show_all()


if __name__ == '__main__':
    main()
