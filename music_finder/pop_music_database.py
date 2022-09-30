#!/usr/bin/env python3
import sqlite3
from typing import List

import pyodbc


class PopMusicDatabase:

    def __init__(self, database_path: str = 'pop.db'):
        self._connection = pyodbc.connect("Driver=SQLite3;Database="f"{database_path}")
        self._cursor = self._connection.cursor()
        pass

    def show_all(self):
        self._cursor.execute("select artist from pop")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def show_all(self):
        self._cursor.execute("select artist from pop")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def add_one_artist(self, artist: str):
        self._cursor.execute("insert into pop (artist_name) values (?)", artist)
        self._connection.commit()

    def add_many_artists(self, list: List[str]):
        self._cursor.executemany("insert into pop values (?)", list)
        self._connection.commit()

    def delete_artist(self, artist: str):
        self._cursor.execute("delete from pop where artist_name = ?", artist)
        self._connection.commit()

    def artist_lookup_by_name(self, artist: str):
        self._cursor.execute("select artist_name from pop where artist_name = ?", artist)
        for row in self._cursor:
            print(row.artist_name)

    def choose_random_artist(self):
        self._cursor.execute("select artist_name from pop order by random()")
        item = self._cursor.fetchone()
        print(item.artist_name)
