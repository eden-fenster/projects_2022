#!/usr/bin/env python3
from music_finder.music_database import MusicDatabase


def genre_template(name: str):
    default_database_name = f'{name}.db'
    default_table_name: str = f"{name}"
    class_name: str = default_table_name[0].toUpper() + default_table_name[1:] + 'MusicDatabase'
class_name = "xxx"
class f"{class_name}"(MusicDatabase):
    def __init__(self):
        super().__init__(database_path=default_database_name, table_name=default_table_name)
    pass
