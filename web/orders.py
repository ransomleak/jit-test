import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/orders")
def orders():
    conn = sqlite3.connect("app.db")
    customer = request.args["customer"]
    return str(conn.execute("SELECT id FROM orders WHERE customer = '" + customer + "'").fetchall())
