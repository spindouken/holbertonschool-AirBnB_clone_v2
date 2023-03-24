#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0:5000"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def holla_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnbbb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_meh(text):
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'},
            strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_awesome(text):
    return "Python " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
