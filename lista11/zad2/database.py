import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, path: str) -> None:
        self.connection = sqlite3.connect(path)
        print(f"db in {path} connected successfully")
        self.cursor = self.connection.cursor()

    def run_query(self, query: str):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Error as err:
            print(f"caught {err}, query didn't complete")

    def run_read_query(self, query: str):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as err:
            print(f"caught {err}, query didn't complete, no results")
