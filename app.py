import ast
import os
import sqlite3

from flask import Flask, request

from utils import total_price

app = Flask(__name__)

DB_PASSWORD = "rd-demo-hunter2-not-real"


def get_db():
    return sqlite3.connect("app.db")


@app.route("/user")
def user():
    name = request.args.get("name")
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")
    return str(cur.fetchall())


@app.route("/calc")
def calc():
    expr = request.args.get("expr")
    return str(ast.literal_eval(expr))


@app.route("/ping")
def ping():
    host = request.args.get("host")
    os.system("ping -c 1 " + host)
    return "ok"


@app.route("/total")
def total():
    items = request.get_json() or []
    return str(total_price(items))


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG") == "1")
