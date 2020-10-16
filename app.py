from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import pandas as pd
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)


@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    data = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    all_measurements = []
    for date, prcp in data:
        measurement_dict = {}
        measurement_dict['date'] = date
        measurement_dict['prcp'] = prcp
        all_measurements.append(measurement_dict)

    return jsonify(all_measurements)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    results = session.query(Station.name, Station.station).all()

    session.close()

    return jsonify(results)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    data = session.query(Measurement.date, Measurement.tobs).all()

    session.close()

    all_temps = []
    for date, tobs in data:
        temps_dict = {}
        temps_dict['date'] = date
        temps_dict['tobs'] = tobs
        all_temps.append(temps_dict)

    return jsonify(all_temps)


@app.route("/api/v1.0/2016-08-23")
def start_date():
    session = Session(engine)

    temp_data = session.query(func.min(Measurement.tobs), func.avg(
        Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    temp_data = list(np.ravel(temp_data))
    session.close()

    return jsonify(results)


@app.route("/api/v1.0/<start>/2017-08-23")
def start_date/end_date():


if __name__ == '__main__':
    app.run(debug=True)
