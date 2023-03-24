#!/usr/bin/python3
"""script that starts a Flask web application
on 0.0.0.0, port 5000"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def holla_holla():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
