from flask import Flask, render_template, request, session
from flask_session import Session


app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    headline = "Hello! World"
    return render_template("index.html", headline=headline)


#@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}!"


@app.route("/buy")
def bye():
    headline = "Hey, Goodbye!"
    return render_template("index.html", headline=headline)

@app.route('/more')
def more():
    return render_template("index1.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)



notes = []

@app.route('/notes1', methods=['GET','POST'])
def notes1():

    if session.get('notes') is None:
        session['notes'] = []
    if request.method == "POST":
        note = request.form.get("note")
        session['notes'].append(note)

    return render_template("note.html", notes=session['notes'])



FLASK_DEBUG=1