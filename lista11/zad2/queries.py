#!/usr/bin/env python3
import random
from sqlite3.dbapi2 import DatabaseError
from typing import Any


from rich.console import Console
from rich.rule import Rule
from rich.table import Table
from rich.traceback import install

import database as db
import pathlib

DB_PATH = pathlib.Path(
    "/home/ashley/wstep-do-prog-sem1/lista11/zad2/mydb.sqlite")


# Output prettifier
console = Console()
install()
# catch the lack of a file or a bad suffix
if not (DB_PATH.exists() or DB_PATH.suffix == ".sqlite"):
    raise FileNotFoundError(f"expected an sqlite file path (got {DB_PATH})")

# using my Database helper object to load the db as a context and close it when I'm done
with db.Database(DB_PATH) as db:

    console.print(Rule("DB loaded correctly.", align="left"))

    # a query that gets all users
    get_all_users = """
    SELECT name
    FROM users;
    """
    users = db.run_read_query(get_all_users)
    if not users:
        raise DatabaseError("database should contain users")
    # take a random user, we'll use them to display the results
    randuser = users[random.randint(1, len(users)) - 1][0]

    # get all posts made by the user
    get_posts_from_user = f"""
    SELECT posts.id, posts.content
    FROM posts, users
    WHERE posts.user_id = users.id AND users.name IS "{randuser}"
    """
    user_posts: list[Any] = db.run_read_query(get_posts_from_user)
    if not user_posts:
        console.print("[bold red]No posts by this person[/]")
    else:
        # rendering a Rich table
        table = Table(title=f":pencil: Posts by [blue]{randuser}[/]")
        table.add_column("[red bold]Post ID[/]", style="red")
        table.add_column("Post content")
        for id, content in user_posts:
            table.add_row(str(id), content)
        console.print(table)

    # get the count of posts by the user
    get_postcount_from_user = f"""
    SELECT COUNT(*), users.name
    FROM posts, users
    WHERE posts.user_id = users.id AND users.name IS "{randuser}"
    """
    postcount = db.run_read_query(get_postcount_from_user)
    if postcount:
        count, name = postcount[0]
        console.print(
            f"[blue italic]\n{name}[/] has made {count} posts.")

    # get average length of posts by the user
    get_users_avglen = f"""
    SELECT AVG(length(posts.content)), users.name
    FROM posts, users
    WHERE posts.user_id = users.id AND users.name IS "{randuser}"
    """
    avglen = db.run_read_query(get_users_avglen)[0][0]
    console.print(
        f"Their average post is [green bold]{avglen:.2f}[/] characters long.")

    # delete the selected user
    delete_user = f"""
    DELETE FROM users
    WHERE name = "{randuser}";
    """
    db.run_query(delete_user)

    # show that all of the posts that were orphaned (their user_id was set to NULL
    # because of the 'ON DELETE SET NULL' constraint)
    get_orphaned_posts = f"""
    SELECT DISTINCT posts.id, posts.content
    FROM posts, users
    WHERE posts.user_id IS NULL;
    """
    orphaned_posts: list[Any] = db.run_read_query(get_orphaned_posts)
    if not orphaned_posts:
        console.print("[bold red]No orphaned posts[/]")
    else:
        table = Table(title=f":ghost: orphaned posts")
        table.add_column("[red bold]Post ID[/]", style="red")
        table.add_column("Post content")
        for id, content in orphaned_posts:
            table.add_row(str(id), content)
        console.print(table)
