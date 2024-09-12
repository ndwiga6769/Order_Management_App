from flask import request, jsonify
from flask_jwt_extended import create_access_token

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'admin':  # Basic validation; replace with OpenID Connect
        access_token = create_access_token(identity={'username': data['username']})
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401
