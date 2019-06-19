import os
from flask import jsonify

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

DATABASE_URL = 'sqlite:///C:/sqlitedatabase/test1.db';
engine = create_engine((DATABASE_URL))
db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("flight.html", flights=flights)

@app.route("/book", methods=['POST'])
def book():
    """Book Flight"""

    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid Flight Number")

    if db.execute("SELECT * FROM flights WHERE id=:id", {"id":flight_id}).rowcount ==0:
        return render_template("error.html", message='No Such Flight with this Id')
    db.execute("INSERT INTO passengers(name, flight_id) VALUES(:name, :flight_id)",
        {'name':name, 'flight_id':flight_id})

    db.commit()
    return render_template("success.html")


@app.route('/flights')
def flights():
    """ List of all flights"""
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("flights.html", flights=flights)


@app.route('/flights/<int:flight_id>')
def flight(flight_id):
    """ List Details about single flight"""
    flight = db.execute("SELECT * FROM flights WHERE id =:id",{'id':flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message='No such flight')

    passengers =  db.execute("SELECT name FROM passengers WHERE flight_id= :flight_id",
                             {"flight_id": flight_id}).fetchall()
    return render_template("flight1.html", flight=flight, passengers=passengers)


@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    """Return Detail about a single flight"""
    # make sure flight exists.
    flight = db.execute("SELECT * FROM flights WHERE id =:id", {'id': flight_id}).fetchone()
    if flight is None:
        return jsonify({"error": "Invalid flight_id"}), 422

    # Get all passengers
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id= :flight_id",
                             {"flight_id": flight_id}).fetchall()
    names=[]
    for passenger in passengers:
        names.append(passenger.name)
    data = {
        "origin": flight.origin,
        "destination":flight.destination,
        "duration": flight.duration,
        "passengers": names
    }
    return jsonify(data)

