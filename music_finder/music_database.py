from typing import List

import pyodbc


class MusicDatabase:
    def __init__(self, database_path: str, table_name: str):
        connection_string = "Driver=SQLite3;Database="f"{database_path}"
        self._connection = pyodbc.connect(connection_string)
        self._cursor = self._connection.cursor()
        self.table_name = table_name
        pass

    def show_all(self):
        self._cursor.execute(f'select artist from {self.table_name}')
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def add_one_artist(self, artist: str):
        self._cursor.execute(f'insert into {self.table_name} (artist_name) values (?)', artist)
        self._connection.commit()

    def add_many_artists(self, artist_list: List[str]):
        self._cursor.executemany(f'insert into {self.table_name} values (?)', artist_list)
        self._connection.commit()

    def delete_artist(self, artist: str):
        self._cursor.execute(f'delete from {self.table_name} where artist_name = ?', artist)
        self._connection.commit()

    def artist_lookup_by_name(self, artist: str):
        self._cursor.execute(f'select artist_name from {self.table_name} where artist_name = ?', artist)
        for row in self._cursor:
            print(row.artist_name)

    def choose_random_artist(self):
        self._cursor.execute(f'select artist_name from {self.table_name} order by random()')
        item = self._cursor.fetchone()
        print(item.artist_name)
