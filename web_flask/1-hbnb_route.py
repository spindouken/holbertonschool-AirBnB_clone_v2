#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0:5000"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def holla_holla():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
