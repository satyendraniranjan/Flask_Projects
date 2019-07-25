Flight Booking
====================

**Flask is a micro web framework written in Python**.

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]

Overview
====================

**Best attempt** to create small project on **Flight Booking**.



How to install Virtual Envoirnment
==================================
A step by step series of examples that tell you how to get a development env running

Before we install Flask, create a virtual environment (also called a virtualenv)

```
python -m venv myvenv
```

The command above will create a directory called myvenv (or whatever name you chose) that contains our virtual environment (basically a bunch of directory and files).
Start your virtual environment by running:

```
$ myvenv\Scripts\activate
```
Now that you have your virtualenv started, you can install Django.
Before we do that, we should make sure we have the latest version of pip, the software that we use to install Django:

```
(myvenv) ~$ python -m pip install --upgrade pip
```


How to install Flask
==================================

To install flask run this command on your cmd.

```
pip install flask

```
Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.

To install flask-SQLAlchemy run this command on your cmd.
```
pip install flask_sqlalchemy

```



How to install SQlite
==================================

Download SQlite from here.

* [Database](https://www.sqlite.org/download.html) - SQLite

After downloading SQlite extract it and add path to your Envoirnment Variable for this.
To use it type 


```
sqlite3 nameofdatabase.db.
```



How to use
====================

There are three main files in this project to run.
1) FlightBooking File
On Windows you should run the following command to Run Project. 
```
(myvenv) C:\Path to Project>set FLASK_DEBUG=1
(myvenv) C:\Path to Project>set FLASK_APP=P2.py
(myvenv) C:\Path to Project>flask run

```

**API for Flight Booking**

=======================

Build API for Flight Booking:
url for using this api.
```
url/api/flights/number(flight detail of which you want)

```
it will return jason response

```
http://127.0.0.1:5000/api/flights/1
response for this:

{"destination":"Mumbai","duration":416,"origin":"New Delhi","passengers":["ALICE","Bob","Satyendra Niranjan","Satyendra","New Passenger"]}

```



2) CurrencyConverter File
On Windows you should run the following command to Run Project. 
```
(myvenv) C:\Path to Project>set FLASK_DEBUG=1
(myvenv) C:\Path to Project>set FLASK_APP=P2.py
(myvenv) C:\Path to Project>flask run

```


3) Vote File
On Windows you should run the following command to Run Project. 
```
(myvenv) C:\Path to Project>set FLASK_DEBUG=1
(myvenv) C:\Path to Project>set FLASK_APP=P2.py
(myvenv) C:\Path to Project>flask run --no-reload 

```




Running the tests
====================

To run the tests against the current environment:

    python test.py




Version
====================
* [Python 3.7.1](https://www.python.org/downloads/release/python-370/) - Programming Language
* [Flask 2.0.0](http://flask.pocoo.org/) - The Web Framework
* [Database](https://www.sqlite.org/download.html) - SQLite
* [HTML 5](https://www.python.org/downloads/release/python-370/) - Front end language
* [CSS 3](https://docs.djangoproject.com/en/2.2/releases/2.0/) - Front end language

