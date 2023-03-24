#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0:5000
"""
from flask import Flask, render_template
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
    """
    display “Python ” followed by the value of the text variable
    and replace underscore _ symbols with a space
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def aintnothinbutanumba(numba):
    """display "n is a number" only if n is an interger"""
    return "{} is a number".format(numba)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(numba):
    return render_template('5-number.html', numba=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
