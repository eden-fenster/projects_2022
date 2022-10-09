#!/usr/bin/env python3
import sqlite3


def create_database(name: str):
    conn = sqlite3.connect(f'{name}.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE f'{name}' (
    artist_name text
    )""")
    conn.commit()
    conn.close()
