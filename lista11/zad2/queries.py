import random
from sqlite3.dbapi2 import DatabaseError
from typing import Any

from rich.console import Console
from rich.rule import Rule
from rich.table import Table
from rich.traceback import install

import database as db

DB_PATH = "/home/ashley/wstep-do-prog-sem1/lista11/zad2/mydb.sqlite"

console = Console()
install()

with db.Database(DB_PATH) as db:
    console.print(Rule("DB loaded correctly.", align="left"))
    get_all_users = """
    SELECT name
    FROM users;
    """

    users = db.run_read_query(get_all_users)
    if not users:
        raise DatabaseError("database should contain users")

    randuser = users[random.randint(1, len(users)) - 1][0]

    get_posts_from_random_user = f"""
    SELECT posts.id, posts.content
    FROM posts, users
    WHERE posts.user_id = users.id AND users.name IS "{randuser}"
    """

    randuser_posts: list[Any] = db.run_read_query(get_posts_from_random_user)
    if not randuser_posts:
        console.print("[bold red]No posts by this person[/bold red]")
    else:
        table = Table(title=f":pencil: Posts by [blue]{randuser}[/blue]")
        table.add_column("[red bold]Post ID[/red bold]", style="red")
        table.add_column("Post content")

        for id, content in randuser_posts:
            table.add_row(str(id), content)
        console.print(table)

    get_postcount_from_random_user = f"""
    SELECT COUNT(*), users.name
    FROM posts, users
    WHERE posts.user_id = users.id AND users.name IS "{randuser}"
    """
    postcount = db.run_read_query(get_postcount_from_random_user)
    if postcount:
        count, name = postcount[0]
        console.print(
            f"[blue italic]\n{name}[/blue italic] has made {count} posts.")
