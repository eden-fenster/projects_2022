#!/usr/bin/env python3
from typing import Tuple, List

from music_finder_database import MusicFinderDatabase
from music_database import MusicDatabase
from database_template import create_database

genre_list = MusicFinderDatabase()
rock_database = MusicDatabase()
pop_database = MusicDatabase()


def main() -> None:
    print('Good day, what do you want to do today ?')
    add_genre: str = input('Do you want to add a genre ? type Yes for yes and No for no  \n')
    add_artist: str = input('Do you want to add an artist ? type Yes for yes and No for no  \n')
    lookup_genre: str = input('Do you want to look up a genre ? type Yes for yes and No for no  \n')
    lookup_artist: str = input('Do you want to look up an artist ? type Yes for yes and No for no  \n')
    delete_genre: str = input('Do you want to delete a genre ? type Yes for yes and No for no  \n')
    # delete_artist: str = input('Do you want to delete an artist ? type Yes for yes and No for no  \n')
    print_genre_or_not: str = input('Do you want to return a genre ? type Yes for yes and No for no  \n')
    # print_artist_or_not: str = input('Do you want to return an artist ? type Yes for yes and No for no  \n')

    if add_genre == 'Yes':
        add_a_genre()

    if add_artist == 'Yes':
        add_an_artist()

    if delete_genre == 'Yes':
        delete_a_genre()

    if lookup_genre == 'Yes':
        lookup_a_genre()

    if lookup_artist == 'Yes':
        lookup_an_artist()

    if print_genre_or_not == 'Yes':
        print_genre()

    # if print_artist_or_not == 'Yes':
    #     print_artist()


def print_genre():
    random_or_all: str = \
        input('Do you want a random genre or all genres printed ? type Random for random and All for all \n')
    if random_or_all == 'Random':
        print(genre_list.choose_random_genre())
        return
    if random_or_all == 'All':
        print(genre_list.show_all())


def lookup_a_genre():
    name: str = input('Type name of genre \n')
    print(genre_list.genre_lookup(name))


def lookup_an_artist():
    name: str = input('Type name of artist \n')
    genre: str = input('Type genre of artist \n')
    if genre == 'rock':
        rock_database.artist_lookup_by_name(artist=name)
    if genre == 'pop':
        pop_database.artist_lookup_by_name(artist=name)


def delete_a_genre():
    genre_to_delete: str = input('What genre do you want to delete ? \n')
    genre_list.delete_genre(genre_to_delete)
    print(genre_list.show_all())


def add_a_genre():
    num: int = int(input('How many genres do you want to add ? \n'))
    while num < 1:
        num: int = int(input('Not a valid number, try again ! \n'))

    num_to_add: int = int(num)
    if num_to_add == 1:
        exist: bool = bool(input('Does the database exist ? \n'))
        if not exist:
            genre_name: str = input('Input genre name \n')
            create_database(name=genre_name)
        genre_name: str = input('Input genre name \n')
        genre_url: str = input('Input URL of database \n')

        genre_list.add_genre(genre_name, genre_url)
        print(genre_list.genre_lookup(genre_name))
        return

    genres_to_add: List[Tuple[str, str]] = []

    for i in range(0, num_to_add):
        genre_name: str = input('Input genre name \n')
        exist: bool = bool(input('Does the database exist ? \n'))
        if not exist:
            genre_name: str = input('Input genre name \n')
            create_database(name=genre_name)
        genre_url: str = input('Input URL of database \n')
        genre: Tuple[str, str] = (genre_name, genre_url)
        genres_to_add.append(genre)
        genre_list.add_many_genres(genres_to_add)


def add_an_artist():
    num: int = int(input('How many artists do you want to add ? \n'))
    while num < 1:
        num: int = int(input('Not a valid number, try again ! \n'))

    num_to_add: int = int(num)
    if num_to_add == 1:
        artist_name: str = input('Input artist name \n')
        genre_name: str = input('Input genre name \n')
        if genre_name == 'rock':
            rock_database.add_one_artist(artist=artist_name)
            print(rock_database.artist_lookup_by_name(artist=artist_name))
            return
        if genre_name == 'pop':
            pop_database.add_one_artist(artist=artist_name)
            print(pop_database.artist_lookup_by_name(artist=artist_name))
            return

    rock_artists_to_add: List[str] = []
    pop_artists_to_add: List[str] = []

    for i in range(0, num_to_add):
        artist_name: str = input('Input artist name \n')
        genre_name: str = input('Input genre name \n')
        if genre_name == 'rock':
            rock_artists_to_add.append(artist_name)
        if genre_name == 'pop':
            pop_artists_to_add.append(artist_name)

        rock_database.add_many_artists(artist_list=rock_artists_to_add)
        pop_database.add_many_artists(artist_list=pop_artists_to_add)


if __name__ == '__main__':
    main()
