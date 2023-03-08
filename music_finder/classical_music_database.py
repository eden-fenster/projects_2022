#!/usr/bin/env python3
from music_finder.music_database import MusicDatabase

DEFAULT_DATABASE_NAME = 'classical.db'
DEFAULT_TABLE_NAME = "classical"


class ClassicalMusicDatabase(MusicDatabase):
    def __init__(self):
        super().__init__(database_path=DEFAULT_DATABASE_NAME, table_name=DEFAULT_TABLE_NAME)

    pass
