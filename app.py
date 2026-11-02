import sqlite3


def get_user(conn, user_id):
    return conn.execute("SELECT name FROM users WHERE id = ?", (user_id,)).fetchone()
