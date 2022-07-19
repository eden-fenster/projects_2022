import sqlite3
# Create a table
# conn = sqlite3.connect('bul_pgia_records.db')

# Create a cursor
# c = conn.cursor()
# c.execute("""CREATE TABLE bul_pgia_records (
#   generated_number integer,
#   guessed text
#   )""")


# Add a new record to the table
class BulPgiaDatabase:

    def __init__(self, database_path: str):
        self._connection = sqlite3.connect(database_path)
        self._cursor = self._connection.cursor()
        pass

    def show_all(self):
        self._cursor.execute("SELECT rowid, * FROM bul_pgia_records")
        items = self._cursor.fetchall()
        for item in items:
            print(item)

    def add_one(self, number: int, guessed: str):
        self._cursor.execute("INSERT INTO customers VALUES (?, ?)", (number, guessed))
        self._connection.commit()
        self._connection.close()
