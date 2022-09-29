#!/usr/bin/env python3
import sqlite3

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

# Update records
# c.execute("""UPDATE customers SET first_name = 'Mary'
# WHERE rowid = 3
# """)

# Delete records
# c.execute("DELETE from customers WHERE rowid = 6")

# conn.commit()

# many_customers = [
# ('John', 'Elder', 'john@codemy.com'),
# ('Tim', 'Smith', 'tim@codemy.com'),
# ('Mary', "Brown", 'mary@codemy.com'),
# ('Wes', 'Brown', 'wes@brown.com'),
# ('Steph', 'Kuewa', 'steph@kuewa.com')

# ]


# Create a table
# c.execute("""CREATE TABLE genres (
# genre text,
# database_url text
# )""")

# Insert a record into the table
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")

# Insert many
# c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)


# Query the Database
# rowid prints the ids, WHERE lets me decides to only print things that match what we want,
# LIKE finds everything that matches it.
# c.execute("SELECT rowid, * FROM customers ")

# Order by - ORDER BY, DESC - descending, ASC - ascending.
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

# And - AND/Or - OR
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3")

# Limit - LIMIT
# c.execute("SELECT rowid, * FROM customers LIMIT 3")

# Deleting table - DROP TABLE + name
# c.execute("DROP TABLE customers")
# conn.commit()

# It's a tuple so add [] to get only one type of data

# Fetch the first item
# print(c.fetchone())

# Fetch a selected number of items
# print(c.fetchmany(3))

# Fetch all
# print(c.fetchall())

# items = c.fetchall()

# print("NAME " + "\t\tEMAIL")
# print("-----" + "\t\t--------")
# for item in items:
# print(item[0] + " " + item[1] + '\t' + item[2])
# print(item)

# One line
# c.execute("CREATE TABLE customers (first_name DATATYPE, last_name, DATATYPE, email_address, DATATYPE)")

# Types: NULL, INTEGER, REAL(decimal), TEXT and BLOB(exactly as it is).

# Commit out command
# conn.commit()

# Close our connection
# conn.close()
