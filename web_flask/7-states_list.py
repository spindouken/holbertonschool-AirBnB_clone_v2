#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML page with a list of all states objects
    present in DBStorage sorted by name"""
    states = storage.all(State)
    sorted_states_list = sorted(states.values(), key=lambda state: state.name)
    print("sorted_states_list:", sorted_states_list)
    return render_template('7-states_list.html', states=sorted_states_list)

@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
