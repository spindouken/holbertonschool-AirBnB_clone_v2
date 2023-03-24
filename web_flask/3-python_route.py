#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0:5000"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def holla_holla():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text_value(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text_value(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
