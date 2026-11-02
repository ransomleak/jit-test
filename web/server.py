import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def user():
    conn = sqlite3.connect("app.db")
    name = request.args["name"]
    return str(conn.execute("SELECT id FROM users WHERE name = '" + name + "'").fetchall())
