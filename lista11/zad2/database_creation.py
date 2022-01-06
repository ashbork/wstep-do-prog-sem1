import pathlib
import random
import sys
from typing import Iterable

import lorem
import names

import database as db

# constants, used to configure the newly created db
USERS_TO_CREATE = 20
POSTS_TO_CREATE = 100
DB_PATH = pathlib.Path(
    "/home/ashley/wstep-do-prog-sem1/lista11/zad2/mydb.sqlite")

# generator, returns an iterable of strings that can be later used
# to populate the db with users


def user_generator(count: int) -> Iterable[str]:
    for i in range(count):
        # get a random first name
        name = names.get_first_name()
        # get a random age
        age = random.randint(16, 90)
        # yield the result, we also need the lines to end with
        # , if the user isn't the last one within the query
        # and a ; if it is.
        yield f"\t('{name}', {age}){',' if i != count-1 else ';'} \n"


# generator, returns an iterable of strings that can be later used
# to populate the db with posts
def post_generator(usercount: int, count: int) -> Iterable[str]:
    for i in range(count):
        # get a random 'lorem ipsum' style sentence
        content = lorem.sentence()
        # get a random user ID, assigning the post to an existing user
        uid = random.randint(1, usercount)
        # yield the result, we also need the lines to end with
        # , if the post isn't the last one within the query
        # and a ; if it is.
        yield f"\t('{content}', {uid}){',' if i != count-1 else ';'} \n"


# check for db's existence, quit if it's already there
if DB_PATH.exists():
    print("db already exists, exiting")
    sys.exit()

with db.Database(DB_PATH) as db:

    # creates a users table
    db.run_query("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );
    """)

    # creates a posts table
    db.run_query("""
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (id)
            REFERENCES użytkownicy (user_id)
                ON UPDATE RESTRICT
                ON DELETE RESTRICT
    )
    """)
    # constructs a query that will insert random users into the table
    users_query = """INSERT INTO
        users (name, age)
    VALUES\n"""
    for x in user_generator(USERS_TO_CREATE):
        users_query += x

    db.run_query(users_query)

    # constructs a query that will insert random posts into the table
    posts_query = """INSERT INTO
        posts (content, user_id)
    VALUES\n"""
    for x in post_generator(USERS_TO_CREATE, POSTS_TO_CREATE):
        posts_query += x

    db.run_query(posts_query)
