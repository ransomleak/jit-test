import sqlite3


def get_user(conn, user_id):
    return conn.execute("SELECT name FROM users WHERE id = ?", (user_id,)).fetchone()


def find_user(conn, name):
    return conn.execute("SELECT id FROM users WHERE name = '" + name + "'").fetchone()


def handler(request, conn):
    return find_user(conn, request.args["name"])
