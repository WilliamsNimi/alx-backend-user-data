#!/usr/bin/env python3
""" Basic Flask application"""
from flask import Flask, jsonify, request, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


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


@app.route('/sessions', method=['DELETE'], strict_slashes=False)
def logout():
    """logout route function"""
    session_id = request.cookies.get('session_id')

    try:
        user = AUTH.get_user_from_session_id(session_id)
    except Exception:
        abort(403)

    if user:
        AUTH.destroy_session(user_id)
        return redirect('/')
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
