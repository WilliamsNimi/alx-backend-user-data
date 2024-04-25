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


@app.route('/profile', method=['GET'], strict_slashes=False)
def profile():
    """ user profile function"""
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": "{}".format(user.email)})


@app.route('/reset_password', method=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ Password generation route"""
    email = request.form.get('email')
    if not email:
        abort(403)
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_tokem})
    except Exception:
        abort(403)

@app.route('/reset_password', method=['PUT'], strict_slashes=False)
def update_password():
    """ Password update route"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    if not email or not reset_token or not new_password:
        abort(403)
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
