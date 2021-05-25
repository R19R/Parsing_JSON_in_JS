import logging
from flask import Flask, request, render_template, url_for
import logging, json

from flask.json import jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/successjs', methods= ['POST', 'GET'])
def successjs():
    if request.method =='POST':
        result = request.form
        return render_template('successjs.html', result=result)

@app.route("/successmsg", methods=['GET'])
def msg():
    return jsonify({"success":True})


if __name__=="__main__":
    app.run(debug=True)


#json using Js
#how to get json object from request
#json to dictionary in flask