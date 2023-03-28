#!/usr/bin/python3
"""Script that starts a Flask web application
listening on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display a HTML page with filters for states and amenities"""
    states = storage.all(State)
    sorted_states_list = sorted(states.values(), key=lambda state: state.name)
    amenities = storage.all(Amenity)
    sorted_amenities_list = sorted(amenities.values(), key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=sorted_states_list, amenities=sorted_amenities_list)


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
