#!/usr/bin/env python3
import sqlite3

from typing import List, Tuple


# Create a table
# conn = sqlite3.connect('food.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE food (
# food_name text,
# is_in_house integer
# )""")

class RandomSnackGenerator:
    def __init__(self, database_path: str):
        self._connection = sqlite3.connect(database_path)
        self._cursor = self._connection.cursor()
        pass

    def show_all(self):
        self._cursor.execute("SELECT rowid, * FROM food")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    # Add a new record to the table
    def add_one(self, food: str, in_house):
        self._cursor.execute("INSERT INTO food VALUES (?, ?)", (food, in_house))
        self._connection.commit()

    # Delete a record from the table
    def delete_one(self, id: str):
        self._cursor.execute("DELETE from food WHERE rowid = (?)", id)
        self._connection.commit()

    # Add many records
    def add_many(self, list: List[Tuple[str, int]]):
        self._cursor.executemany("INSERT INTO food VALUES (?, ?)", list)
        self._connection.commit()

    # Lookup with WHERE
    def food_lookup(self, in_house):
        self._cursor.execute("SELECT * from food WHERE is_in_house = (?)", (in_house,))
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def select_random_food(self):
        self._cursor.execute("SELECT rowid, * FROM food ORDER BY RANDOM() LIMIT 1")
        items = self._cursor.fetchall()
        for item in items:
            print(item)
