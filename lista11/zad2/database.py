import pathlib
import sqlite3
from sqlite3 import Error
from typing import Any


class Database:
    """
    Simple interface for a SQLite database.
    """

    def __init__(self, path: str | pathlib.Path) -> None:
        """
        Constructs a new database object, connecting
        to a given path. If an exception is raised, print it.

        Args:
            path (str | pathlib.Path): path to the database
        """
        self.path = path
        try:
            self.connection = sqlite3.connect(path)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"caught error {e}")

    def __enter__(self):
        """
        Allows us to use the Database object as a context.

        Example:
        with db.Database(DB_PATH) as db:
            db.run_query(query)

        Returns:
            Database: workable Database object
        """
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"caught error {e}")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes the connection after the context is exited
        """
        self.connection.close()

    def run_query(self, query: str):
        """
        Runs a "writing" query on the database; no results are
        returned.

        Args:
            query (str): a SQLite query that's supposed to be ran
        """
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Error as err:
            print(f"caught {err}, query didn't complete")

    def run_read_query(self, query: str) -> list[Any]:
        """
        Runs a "reading" query; results are returned.

        Args:
            query (str): a SQLite query that's supposed to be ran

        Returns:
            list[Any]: results of the query
        """
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as err:
            print(f"caught {err}, query didn't complete, no results")
            return []
