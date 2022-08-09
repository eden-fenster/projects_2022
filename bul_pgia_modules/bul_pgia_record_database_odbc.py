import pyodbc


# Add a new record to the table
class BulPgiaDatabase:

    def __init__(self, database_path: str = 'bul_pgia_records.db'):
        self._connection = pyodbc.connect("Driver=SQLite3;Database="f"{database_path}")
        self._cursor = self._connection.cursor()
        pass

    def show_all(self):
        self._cursor.execute("select rowid, * from bul_pgia_records")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def add_one(self, number: int, guessed: str, guesses: int):
        self._cursor.execute("insert into bul_pgia_records (number, guessed, guesses) values (?, ?, ?)"
                             , number, guessed, guesses)
        self._connection.commit()
