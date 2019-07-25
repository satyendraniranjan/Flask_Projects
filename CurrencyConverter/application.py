from flask import Flask, render_template, request, session, jsonify
import requests


app = Flask(__name__)




@app.route("/")
def index():
    return render_template("indexnew.html")


@app.route("/convert", methods=["POST"])
def convert():

    #Query for currency exchange rate
    currency = request.form.get("currency")
    res = requests.get('http://data.fixer.io/api/latest?access_key=0c00afc6958b60437fd95d839bf80583',
                       params={"base": "EUR", "symbols": currency})
    #make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success":False})

    #make sure currency is in response
    data = res.json()
    if currency not in data['rates']:
        return jsonify({"success":False})

    return jsonify({"success":True, "rate":data["rates"][currency]})
