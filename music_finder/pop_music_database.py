#!/usr/bin/env python3
from music_finder.music_database import MusicDatabase

DEFAULT_DATABASE_NAME = 'pop.db'
DEFAULT_TABLE_NAME = "pop"


class PopMusicDatabase(MusicDatabase):
    def __init__(self):
        super().__init__(database_path=DEFAULT_DATABASE_NAME, table_name=DEFAULT_TABLE_NAME)

    pass
