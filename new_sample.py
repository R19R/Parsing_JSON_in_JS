from flask import Flask, request, jsonify, render_template, abort, make_response


app = Flask(__name__)

user_dict = [{"id": 1, "name": "Rahul", "age":22 }, 
                {"id": 2, "name": "Luhar", "age":32},
                {"id": 3, "name": "ahrul", "age":35 },
                {"id": 4, "name": "ulahul", "age":92 } ]


@app.route('/')
def home():
    return "Welcome"


@app.route("/users", methods=['GET'])
def users():
    return jsonify(user_dict)

@app.route("/users/<id>", methods=['GET'])
def user_by_id(id):
    for user in user_dict:
        if user['id'] == int(id):
            return jsonify(user)

# @app.route("/users", methods=['POST'])
# def post_user():
#     user = request.form
#     name = request.form['name']
#     age = request.form['age']
#     user['id'] = len(user_dict) + 1
#     user_dict.append(user)
#     return render_template('sample.html', name=name, age=age)


@app.route("/users", methods=["POST"])
def create_user():
    obj = request.get_json()
    if not obj or not 'name' in obj:
        return abort(400)
    userdict = {
        'id': user_dict[-1]['id'] + 1,
        'name': obj.get('name'),
        'age': obj.get('age')
    }
    user_dict.append(userdict)
    return jsonify(user_dict), 201
    


@app.route("/users/<id>", methods=['DELETE'])
def delete_user(id):
    for user in user_dict:
        if user['id'] == int(id):
            user_dict.remove(user)
    return {}

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"Error": "Not found"}), 404)  

if __name__ == "__main__":
    app.run(debug=True)