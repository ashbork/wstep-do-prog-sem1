import random
from sqlite3.dbapi2 import DatabaseError

import database as db

DB_PATH = "/home/ashley/wstep-do-prog-sem1/lista11/zad2/mydb.sqlite"


with db.Database(DB_PATH) as db:
    get_all_users = """
    SELECT name
    FROM users;
    """

    users = db.run_read_query(get_all_users)
    if not users:
        raise DatabaseError("database should contain users")

    randuser = users[random.randint(1, len(users))][0]

    get_posts_from_random_user = f"""
    SELECT posts.id, posts.content
    FROM posts, users
    WHERE posts.user_id = users.id AND users.name IS "{randuser}"
    """

    randuser_posts = db.run_read_query(get_posts_from_random_user)
    if not randuser_posts:
        print("No posts by this person")
    else:
        print(f"Posts by: {randuser}")
        for x in randuser_posts:
            print(x)

    get_postcount_from_random_user = f"""
    SELECT COUNT(*), users.name
    FROM posts, users
    WHERE posts.user_id = users.id AND users.name IS "{randuser}"
    """
    postcount = db.run_read_query(get_postcount_from_random_user)
    if postcount:
        count, name = postcount[0]
        print(f"\n{name} has made {count} posts.")
