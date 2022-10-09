#!/usr/bin/env python3
from typing import Tuple, List

from music_finder_database import MusicFinderDatabase
from music_database import MusicDatabase

music_list = MusicFinderDatabase()
single_genre_database = MusicDatabase()


def main() -> None:
    print('Good day, what do you want to do today ?')
    add_genre: str = input('Do you want to add a genre ? type Yes for yes and No for no  \n')
    add_artist: str = input('Do you want to add an artist ? type Yes for yes and No for no  \n')
    lookup_genre: str = input('Do you want to look up a genre ? type Yes for yes and No for no  \n')
    lookup_artist: str = input('Do you want to look up an artist ? type Yes for yes and No for no  \n')
    delete_genre: str = input('Do you want to delete a genre ? type Yes for yes and No for no  \n')
    delete_artist: str = input('Do you want to delete an artist ? type Yes for yes and No for no  \n')
    print_genre_or_not: str = input('Do you want to return a genre ? type Yes for yes and No for no  \n')
    print_artist_or_not: str = input('Do you want to return an artist ? type Yes for yes and No for no  \n')

    if add_or_not == 'Yes':
        add_a_snack()

    if delete_or_not == 'Yes':
        delete_a_snack()

    if lookup_genre == 'Yes':
        lookup_a_genre()

    if print_genre_or_not == 'Yes':
        print_genre()

    if change_or_not == 'Yes':
        change_the_availability()


def print_genre():
    random_or_all: str = \
        input('Do you want a random genre or all genres printed ? type Random for random and All for all \n')
    if random_or_all == 'Random':
        print(music_list.choose_random_genre())
        return
    if random_or_all == 'All':
        print(music_list.show_all())


def lookup_a_genre():
    name: str = input('Type name of genre \n')
    print(music_list.genre_lookup(name))


def delete_a_snack():
    food_to_delete: str = input('What food do you want to delete ? \n')
    food_list.delete(food_to_delete)
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
