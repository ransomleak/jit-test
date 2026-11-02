import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/search")
def search():
    conn = sqlite3.connect("app.db")
    q = request.args["q"]
    return str(conn.execute("SELECT id FROM items WHERE title = '" + q + "'").fetchall())
