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

    parser.add_argument('-d',
                        '--delete_snack',
                        help='Delete a snack',
                        default=False,
                        action='store_true')

    parser.add_argument('-l',
                        '--lookup_snacks',
                        help='Search for snacks based on availability',
                        default=False,
                        action='store_true')

    parser.add_argument('-s',
                        '--show_snacks',
                        help='Return snacks',
                        default=True,
                        action='store_True')

    parser.add_argument('-c',
                        '--change_availability',
                        help='change the availability status',
                        default=False,
                        action='store_true')

    return parser.parse_args()


def main() -> None:
    args = get_args()
    add_snack: bool = args.add_snack
    delete_snack: bool = args.delete_snack
    lookup_snacks: bool = args.lookup_snacks
    print_snacks: bool = args.show_snacks
    change_availability: bool = args.change_availability

    if add_snack:
        num: str = input('How many snack do you want to add ?') + '\n'
        while not num.isdigit() or int(num) < 1:
            num: str = input('Not a vaild number, try again !') + '\n'
        num_to_add: int = int(num)
        if num_to_add == 1:
            snack_name: str = input('Input snack name') + '\n'
            snack_availability: str = input('Type True for yes and False for no') + '\n'
            food_list.add_one(snack_name, snack_availability)
        if num_to_add > 1:
            snacks_to_add: List[Tuple[str, str]] = []
            for i in range(0, num_to_add):
                snack_name: str = input('Input snack name') + '\n'
                snack_availability: str = input('Type True for yes and False for no') + '\n'
                snack: Tuple[str, str] = (snack_name, snack_availability)
                snacks_to_add.append(snack)
                food_list.add_many(snacks_to_add)

    if delete_snack:
        food_to_delete: str = input('What food do you want to delete ?') + '\n'
        one_or_all: str = input('Do you want to delete one or all instances ? type One for one and All for all') + '\n'
        if one_or_all == 'One':
            food_list.delete_one(food_to_delete)
        if one_or_all == 'All':
            food_list.delete_many(food_to_delete)

    if lookup_snacks:
        name_or_availability: str = \
            input('Do you want to look up by name or by availability ? '
                  'type Name for name and Availability for availability') + '\n'
        if name_or_availability == 'Name':
            name: str = input('Type name of snack') + '\n'
            food_list.food_lookup_by_name(name)
        if name_or_availability == 'Availability':
            condition: str = input('Type True for available and False for not available') + '\n'
            food_list.food_lookup_by_availability(condition)

    if print_snacks:
        random_or_all: str = \
            input('Do you want a random snack or all snacks printed ? type Random for random and All for all') + '\n'
        if random_or_all == 'Random':
            food_list.choose_random()
        if random_or_all == 'All':
            food_list.show_all()

    if change_availability:
        num: str = input('How many snack do you want to change ?') + '\n'
        while not num.isdigit() or int(num) < 1:
            num: str = input('Not a vaild number, try again !') + '\n'
        num_to_change: int = int(num)
        if num_to_change == 1:
            snack_name: str = input('Input snack name') + '\n'
            snack_availability: str = input('Type True for yes and False for no') + '\n'
            food_list.change_availability(snack_name, snack_availability)
        if num_to_change > 1:
            i: int = 0
            while i < num_to_change:
                snack_name: str = input('Input snack name') + '\n'
                snack_availability: str = input('Type True for yes and False for no') + '\n'
                food_list.change_availability(snack_name, snack_availability)
                i += 1


if __name__ == '__main__':
    main()
