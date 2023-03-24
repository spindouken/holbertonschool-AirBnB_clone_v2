#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0:5000
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def holla_holla():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnbizzle():
    """displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_walk(text):
    """display “C ” followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_yaya(text="is cool"):
    """display “Python ” followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
