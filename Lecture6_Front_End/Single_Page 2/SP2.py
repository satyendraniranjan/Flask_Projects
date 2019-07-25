from flask import Flask, render_template, request, session


app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

texts = ["Single-page apps take content that would ordinarily be on multiple different pages  and combine them into a single page that pulls new information from the server whenever itâ€™s needed (through methods such as AJAX) For a starting point, this application uses multiple pages.",
         "Single-page apps take content that would ordinarily be on multiple different pages (or routes) and combine them into a single page that pulls new information from the server whenever itâ€™s needed (through methods such as AJAX).",
         "Single-page apps take content that would ordinarily be on multiple different pages."]

@app.route("/first")
def first():
  return texts[0]

@app.route("/second")
def second():
  return texts[1]

@app.route("/third")
def third():
  return texts[2]