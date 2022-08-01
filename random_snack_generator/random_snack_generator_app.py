#!/usr/bin/env python3
from typing import Tuple, List

from snack_list_database_sqlalchemy import FoodDatabase

food_list = FoodDatabase()


def main() -> None:

    print('Good day, what do you want to do today ?')
    add_or_not: str = input('Do you want to add a snack ? type Yes for yes and No for no  \n')
    delete_or_not: str = input('Do you want to delete a snack ? type Yes for yes and No for no  \n')
    lookup_or_not: str = input('Do you want to look up a snack ? type Yes for yes and No for no  \n')
    print_or_not: str = input('Do you want to return a snack ? type Yes for yes and No for no  \n')
    change_or_not: str = \
        input('Do you want to change the availability of a snack ? type Yes for yes and No for no  \n')
    if add_or_not == 'Yes':
        add_a_snack()

    if delete_or_not == 'Yes':
        delete_a_snack()

    if lookup_or_not == 'Yes':
        lookup_a_snack()

    if print_or_not == 'Yes':
        print_a_snack()

    if change_or_not == 'Yes':
        change_the_availability()


def change_the_availability():
    num: int = int(input('How many snacks do you want to change ? \n'))
    while num < 1:
        num: int = int(input('Not a valid number, try again ! \n'))

    num_to_change: int = int(num)
    if num_to_change == 1:
        snack_name: str = input('Input snack name \n')
        # Prints the current status of the food for reference.
        print(food_list.food_lookup_by_name(snack_name))
        snack_availability: str = input('Type True for yes and False for no \n')
        food_list.change_availability(snack_name, snack_availability)
        # Prints the current status of the food after we changed it.
        print(food_list.food_lookup_by_name(snack_name))
        return

    i: int = 0
    while i < num_to_change:
        snack_name: str = input('Input snack name \n')
        # Prints the current status of the food for reference.
        print(food_list.food_lookup_by_name(snack_name))
        snack_availability: str = input('Type True for yes and False for no \n')
        food_list.change_availability(snack_name, snack_availability)
        # Prints the current status of the food after we changed it.
        print(food_list.food_lookup_by_name(snack_name))
        i += 1


def print_a_snack():
    random_or_all: str = \
        input('Do you want a random snack or all snacks printed ? type Random for random and All for all \n')
    if random_or_all == 'Random':
        print(food_list.choose_random())
        return
    if random_or_all == 'All':
        print(food_list.show_all())


def lookup_a_snack():
    name_or_availability: str = \
        input('Do you want to look up by name or by availability ? '
              'type Name for name and Availability for availability \n')
    if name_or_availability == 'Name':
        name: str = input('Type name of snack \n')
        print(food_list.food_lookup_by_name(name))
        return
    if name_or_availability == 'Availability':
        condition: str = input('Type True for available and False for not available \n')
        print(food_list.food_lookup_by_availability(condition))


def delete_a_snack():
    food_to_delete: str = input('What food do you want to delete ? \n')
    one_or_all: str = input('Do you want to delete one or all instances ? type One for one and All for all \n')
    if one_or_all == 'One':
        food_list.delete_one(food_to_delete)
        # Prints the current status of the database after we deleted the food.
        print(food_list.show_all())
        return
    if one_or_all == 'All':
        food_list.delete_many(food_to_delete)
        # Prints the current status of the database after we deleted the food.
        print(food_list.show_all())


def add_a_snack():
    num: int = int(input('How many snacks do you want to add ? \n'))
    while num < 1:
        num: int = int(input('Not a valid number, try again ! \n'))

    num_to_add: int = int(num)
    if num_to_add == 1:
        snack_name: str = input('Input snack name \n')
        snack_availability: str = input('Type True for yes and False for no \n')
        food_list.add_one(snack_name, snack_availability)
        # Prints the current status of the food after we added the snack.
        print(food_list.food_lookup_by_name(snack_name))
        return

    snacks_to_add: List[Tuple[str, str]] = []

    for i in range(0, num_to_add):
        snack_name: str = input('Input snack name \n')
        snack_availability: str = input('Type True for yes and False for no \n')
        snack: Tuple[str, str] = (snack_name, snack_availability)
        snacks_to_add.append(snack)
        food_list.add_many(snacks_to_add)


if __name__ == '__main__':
    main()
