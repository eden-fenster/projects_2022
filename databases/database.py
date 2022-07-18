#!/usr/bin/env python3
import sqlite3

# If we don't want to save the database
# conn = sqlite3.connect(':memory:')


# conn = sqlite3.connect('customer.db')

# Create a cursor
# c = conn.cursor()

# Query the database and return all records
from typing import List, Tuple


class Database:
    def __init__(self, database_path: str):
        self._connection = sqlite3.connect(database_path)
        self._cursor = self._connection.cursor()
        pass

    def show_all(self):
        self._cursor.execute("SELECT rowid, * FROM customers")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    # Add a new record to the table
    def add_one(self, first: str, last: str, email: str):
        self._cursor.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
        self._connection.commit()
        self._connection.close()

    # Add a dictionary to the table
    def add_dict(self, dictionary: dict):
        self._cursor.execute("INSERT INTO customers VALUES (:first_name, :last_name, :email_address)", dictionary)
        self._connection.commit()
        self._connection.close()

    # Delete a record from the table
    def delete_one(self, id: str):
        self._cursor.execute("DELETE from customers WHERE rowid = (?)", id)
        self._connection.commit()
        self._connection.close()

    # Add many records
    def add_many(self, list: List[Tuple[str, str, str]]):
        self._cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", list)
        self._connection.commit()
        self._connection.close()

    # Lookup with WHERE
    def email_lookup(self, email: str):
        self._cursor.execute("SELECT * from customers WHERE email_address = (?)", (email,))
        items = self._cursor.fetchall()
        for item in items:
            print(item)

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
# c.execute("""CREATE TABLE customers (
# first_name text,
# last_name text,
# email_address text
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
