import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/users")
def users():
    conn = sqlite3.connect("app.db")
    return str(conn.execute("SELECT id FROM users WHERE email = '" + request.args["email"] + "'").fetchall())
