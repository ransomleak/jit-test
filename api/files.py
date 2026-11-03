import os

from flask import Flask, request, send_file

app = Flask(__name__)


@app.route("/file")
def file():
    return send_file(os.path.join("/srv/data", request.args["name"]))


@app.route("/run")
def run():
    os.system("ping -c 1 " + request.args["host"])
    return "ok"
