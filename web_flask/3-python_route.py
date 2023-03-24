#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0:5000"""
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def holla_holla():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", methods=['GET'], strict_slashes=False)
def hbnb():
    """displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", methods=['GET'], strict_slashes=False)
def c_text_value(text):
    """display “C ” followed by the value of the text variable"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python_text_value(text="is cool"):
    """displays "Python " followed by the text value (of declared variable)"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
