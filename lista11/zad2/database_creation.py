import pathlib
import random
import sys

import lorem
import names

import database as db

USERS_TO_CREATE = 20
POSTS_TO_CREATE = 100
DB_PATH = "/home/ashley/wstep-do-prog-sem1/lista11/zad2/mydb.sqlite"


def user_generator(count):
    for i in range(count):
        name = names.get_first_name()
        age = random.randint(16, 90)
        yield f"\t('{name}', {age}){',' if i != count-1 else ';'} \n"


def post_generator(usercount, count):
    for i in range(count):
        content = lorem.sentence()
        uid = random.randint(1, usercount)
        yield f"\t('{content}', {uid}){',' if i != count-1 else ';'} \n"


if pathlib.Path(DB_PATH).exists():
    print("db already exists, exiting")
    sys.exit()

db = db.Database(DB_PATH)

db.run_query("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);
""")

db.run_query("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (id)
        REFERENCES użytkownicy (user_id)
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
)
""")

users_query = """INSERT INTO
    users (name, age)
VALUES\n"""
for x in user_generator(USERS_TO_CREATE):
    users_query += x

db.run_query(users_query)

posts_query = """INSERT INTO
    posts (content, user_id)
VALUES\n"""
for x in post_generator(USERS_TO_CREATE, POSTS_TO_CREATE):
    posts_query += x

db.run_query(posts_query)
