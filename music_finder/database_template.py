#!/usr/bin/env python3
import sqlite3


def create_database():
    conn = sqlite3.connect('genre.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE genre (
    genre text,
    database_url text
    )""")
    conn.commit()
    conn.close()


create_database()
