import ast
import os
import sqlite3
import subprocess

from flask import Flask, request

from utils import total_price

app = Flask(__name__)

DB_PASSWORD = os.environ.get("DB_PASSWORD", "")


def get_db():
    return sqlite3.connect("app.db")


# Notes for maintainers.
# 01. This file is a deliberately vulnerable demo; see README.
# 02. This file is a deliberately vulnerable demo; see README.
# 03. This file is a deliberately vulnerable demo; see README.
# 04. This file is a deliberately vulnerable demo; see README.
# 05. This file is a deliberately vulnerable demo; see README.
# 06. This file is a deliberately vulnerable demo; see README.
# 07. This file is a deliberately vulnerable demo; see README.
# 08. This file is a deliberately vulnerable demo; see README.
# 09. This file is a deliberately vulnerable demo; see README.
# 10. This file is a deliberately vulnerable demo; see README.
# 11. This file is a deliberately vulnerable demo; see README.
# 12. This file is a deliberately vulnerable demo; see README.
# 13. This file is a deliberately vulnerable demo; see README.
# 14. This file is a deliberately vulnerable demo; see README.
# 15. This file is a deliberately vulnerable demo; see README.
# 16. This file is a deliberately vulnerable demo; see README.
# 17. This file is a deliberately vulnerable demo; see README.
# 18. This file is a deliberately vulnerable demo; see README.
# 19. This file is a deliberately vulnerable demo; see README.
# 20. This file is a deliberately vulnerable demo; see README.
# 21. This file is a deliberately vulnerable demo; see README.
# 22. This file is a deliberately vulnerable demo; see README.
# 23. This file is a deliberately vulnerable demo; see README.
# 24. This file is a deliberately vulnerable demo; see README.
# 25. This file is a deliberately vulnerable demo; see README.
# 26. This file is a deliberately vulnerable demo; see README.
# 27. This file is a deliberately vulnerable demo; see README.
# 28. This file is a deliberately vulnerable demo; see README.
# 29. This file is a deliberately vulnerable demo; see README.

@app.route("/user")
def user():
    name = request.args.get("name")
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users WHERE name = ?", (name,))
    return str(cur.fetchall())


@app.route("/calc")
def calc():
    expr = request.args.get("expr")
    return str(ast.literal_eval(expr))


@app.route("/ping")
def ping():
    host = request.args.get("host")
    subprocess.run(["ping", "-c", "1", host], check=False)
    return "ok"


@app.route("/total")
def total():
    items = request.get_json() or []
    return str(total_price(items))


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG") == "1")
