#!/usr/bin/env python3
""" Password authentication module """
import bcrypt
from db import DB
from user import User
from typing import TypeVar
import uuid


def _hash_password(password: str):
    """ Password hash method
    @password: The password string to be hashed
    Return: returns a salted hash of the pasword
    """
    p_bytes = password.encode('utf-8')
    p_salt = bcrypt.gensalt()
    p_hash = bcrypt.hashpw(p_bytes, p_salt)
    return p_hash


def _generate_uuid():
    """ uuid generating function"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """ Registers the User
        @email: Email of the new user
        @password: password of the new user
        Return: Returns the new User object
        """
        try:
            self._db.find_user_by(email=email)
            user = User(email=email, password=_hashed_password(password))
            self._db.add_user(user)
            return user
        except Exception:
            raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Login validation method
        @email: email of the user
        @password: user password
        Return: Returns True or False
        """
        try:
            user = self._db.find_user_by(email=email)
            p_bytes = password.encode('utf-8')
            return bycrypt.checkpw(p_bytes, user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """ A session creation function
        @email: the email to search for a session for
        Return: Returns session ID
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_db)
            return session_id
        except Exception:
            return None
