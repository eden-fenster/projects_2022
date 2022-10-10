#!/usr/bin/env python3
import sqlite3


def create_database(name: str):
    conn = sqlite3.connect(f'{name}.db')
    c = conn.cursor()
    command = f"""CREATE TABLE {name} (
    artist_name text
    )"""
    print(command)
    c.execute(command)
    conn.commit()
    conn.close()
create_database(name="test001")