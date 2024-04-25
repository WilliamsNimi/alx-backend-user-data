#!/usr/bin/env python3
""" Basic Flask application"""
from flask import Flask, jsonify, request
from auth import Auth
from auth import Auth


AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def getRequest() -> str:
    """basic get request"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """User authentication function
    @email: email of the user
    @password: user password
    Return: Returns nothing
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', method=['POST'], strict_slashes=False)
def login():
    """ Login authentication function"""
    email = request.form.get('email')
    password = request.get('password')
    if AUTH.valid_login(email, password):
        response = make_response(jsonify({
            "email": email, "message": "logged in"}))
        response.set_cookie('session_id', AUTH.create_session(email))
    else:
        abort(401)
    return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
