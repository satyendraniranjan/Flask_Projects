import os

from flask import Flask, render_template, request,session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from models import *
import csv


app = Flask(__name__)

DATABASE_URL = 'sqlite:///C:/sqlitedatabase/test2.db';
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
db.init_app(app)


def main():
    f = open('flights.csv')
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin = origin, destination= destination, duration=duration)
        db.session.add(flight)
        print(f"Added flight from{origin} to {destination} lasting{duration} minutes.")




if __name__ == '__main__':
    with app.app_context():
        main()
        db.session.commit()



