#!/usr/bin/python3
"""Script that starts a Flask web application
listening on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all State objects
    present in DBStorage sorted by name (A->Z) and their cities"""
    states = storage.all(State)
    sorted_states_list = sorted(states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states_list)


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
