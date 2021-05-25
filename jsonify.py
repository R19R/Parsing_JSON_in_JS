from logging import logMultiprocessing
from flask import Flask, json, jsonify, request , redirect, url_for 
import json
from flask.helpers import url_for
from flask.scaffold import _matching_loader_thinks_module_is_package

from flask.templating import render_template


app = Flask(__name__)

@app.route("/")
def home():
    ipl = {"chennai":"csk", "Mumbai": "MI", "Bangalore":"RCB", "Kolkata":"KKR"}
    return render_template('api.html')

@app.route("/api", methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        res = request.form
        food = request.form['food']
        music = request.form['music']
        return jsonify(favFood=food, favMusic=music)#json.dumps error


@app.route('/apijs', methods=['POST',"GET"])
def apijs():
    if request.method == "POST":
        rem = request.form
        return jsonify(rem)




if __name__ == "__main__":
    app.run(debug=True)