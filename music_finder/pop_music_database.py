#!/usr/bin/env python3
import sqlite3

import pyodbc


class RockMusicDatabase:

    def __init__(self, database_path: str = 'pop.db'):
        self._connection = pyodbc.connect("Driver=SQLite3;Database="f"{database_path}")
        self._cursor = self._connection.cursor()
        pass

    def show_all(self):
        self._cursor.execute("select artist from pop")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def add_one(self, food: str, is_in_house: str):
        self._cursor.execute("insert into food (food_name, is_in_house) values (?, ?)", food, is_in_house)
        self._connection.commit()

    def add_many(self, list: List[Tuple[str, int]]):
        self._cursor.executemany("insert into food values (?, ?)", list)
        self._connection.commit()

    def delete(self, food: str):
        self._cursor.execute("delete from food where food_name = ?", food)
        self._connection.commit()

    def food_lookup_by_name(self, food: str):
        self._cursor.execute("select food_name, is_in_house from food where food_name = ?", food)
        for row in self._cursor:
            print(row.food_name, row.is_in_house)

    def food_lookup_by_availability(self, is_in_house: str):
        self._cursor.execute("select food_name, is_in_house from food where is_in_house = ?", is_in_house)
        for row in self._cursor:
            print(row.food_name, row.is_in_house)

    def choose_random(self):
        self._cursor.execute("select food_name, is_in_house from food order by random()")
        item = self._cursor.fetchone()
        print(item.food_name, item.is_in_house)


c.execute("""CREATE TABLE pop (
artist_name text
)""")

# Commit out command
conn.commit()

# Close our connection
conn.close()
