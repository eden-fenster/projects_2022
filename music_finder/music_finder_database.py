#!/usr/bin/env python3
import sqlite3
from typing import List, Tuple

import pyodbc


class MusicFinderDatabase:

    def __init__(self, database_path: str = 'genre.db'):
        self._connection = pyodbc.connect("Driver=SQLite3;Database="f"{database_path}")
        self._cursor = self._connection.cursor()
        pass

    def show_all(self):
        self._cursor.execute("select genre, database_url from genre")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def add_genre(self, genre: str, database_url: str):
        self._cursor.execute("insert into genre (genre, database_url) values (?, ?)", genre, database_url)
        self._connection.commit()

    def add_many_genres(self, list: List[Tuple[str, str]]):
        self._cursor.executemany("insert into genre (?, ?)", list)
        self._connection.commit()

    def delete_genre(self, genre: str):
        self._cursor.execute("delete from genre where genre = ?", genre)
        self._connection.commit()

    def genre_lookup(self, genre: str):
        self._cursor.execute("select genre, database_url from genre where genre = ?", genre)
        for row in self._cursor:
            print(row.genre, row.database_url)

    def choose_random_genre(self):
        self._cursor.execute("select genre, database_url from genre order by random()")
        item = self._cursor.fetchone()
        print(item.genre, item.database_url)


