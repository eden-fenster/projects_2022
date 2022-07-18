import sqlite3

from typing import List, Tuple

# Create a table
# conn = sqlite3.connect('food.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE food (
# food_name text,
# is_in_house integer
# )""")


def show_all():
    conn = sqlite3.connect('food.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM food")
    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()


# Add a new record to the table
def add_one(food: str, in_house):
    conn = sqlite3.connect('food.db')
    c = conn.cursor()
    c.execute("INSERT INTO food VALUES (?, ?)", (food, in_house))
    conn.commit()
    conn.close()


# Delete a record from the table
def delete_one(id: str):
    conn = sqlite3.connect('food.db')
    c = conn.cursor()
    c.execute("DELETE from food WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


# Add many records
def add_many(list: List[Tuple[str, int]]):
    conn = sqlite3.connect('food.db')
    c = conn.cursor()
    c.executemany("INSERT INTO food VALUES (?, ?)", list)
    conn.commit()
    conn.close()


# Lookup with WHERE
def food_lookup(in_house):
    conn = sqlite3.connect('food.db')
    c = conn.cursor()
    c.execute("SELECT * from food WHERE is_in_house = (?)", (in_house,))
    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()


def select_random_food():
    conn = sqlite3.connect('food.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM food ORDER BY RANDOM() LIMIT 1")
    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()
