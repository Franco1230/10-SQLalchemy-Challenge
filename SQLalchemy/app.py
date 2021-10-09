# Dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from datetime import timedelta

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model.
Base = automap_base()

# Reflect the tables.
Base.prepare(engine, reflect = True)

# Save reference to the tables.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session
session = Session(engine)

# Setup Flask
app = Flask(__name__)

#Set Flask Routes
@app.route("/")
def home():
    """List all routes that are available."""
    return (f"Available Routes:<br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f"/api/v1.0/start (enter as YYYY-MM-DD)<br/>"
            f"/api/v1.0/start/end (enter as YYYY-MM-DD/YYYY-MM-DD)")

@app.route("/api/v1.0/precipitation") #Convert query results to a dictionary using `date` as the key and `tobs` as the value
def precipitation():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query Measurement
    results = (session.query(Measurement.date, Measurement.tobs)
                      .order_by(Measurement.date))
    
    # Create a dictionary
    precipitation_date_tobs = []
    for each_row in results:
        dt_dict = {}
        dt_dict["date"] = each_row.date
        dt_dict["tobs"] = each_row.tobs
        precipitation_date_tobs.append(dt_dict)

    return jsonify(precipitation_date_tobs)


@app.route("/api/v1.0/stations") #Return a JSON list of stations from the dataset
def stations():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query Stations
    stations_results = session.query(Station.station, Station.name).all()

    # Convert list of tuples into normal list
    station_details = list(np.ravel(stations_results))

    return jsonify(station_details)

if __name__ == "__main__":
    app.run(debug = True)