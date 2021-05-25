from flask import Flask, request, jsonify, render_template, make_response
import json

from flask.signals import request_finished


app = Flask(__name__)

users_dict= [{"id": 1, "name" : "Rahul", "age": 12}, {"id": 2, "name" : "Luhar", "age": 22}]

@app.route("/")
def home():
    return "Welcome"

@app.route("/users", methods=["GET"])
def users():
    return jsonify(users_dict)


@app.route("/user/<id>", methods=['GET'])
def users_by_id(id):
    for user in users_dict:
        if user[id] == int(id):
            return jsonify(user)
        return {}
    

if __name__ == '__main__':
    app.run()