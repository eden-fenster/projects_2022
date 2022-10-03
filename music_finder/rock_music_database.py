#!/usr/bin/env python3
from music_finder.music_database import MusicDatabase

DEFAULT_DATABASE_NAME = 'rock.db'
DEFAULT_TABLE_NAME = "rock"


class RockMusicDatabase(MusicDatabase):
    def __init__(self):
        super().__init__(database_path=DEFAULT_DATABASE_NAME, table_name=DEFAULT_TABLE_NAME)

    pass
