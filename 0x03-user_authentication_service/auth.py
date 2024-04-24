#!/usr/bin/env python3
""" Password authentication module """
import bcrypt


def _hash_password(password: str):
    """ Password hash method
    @password: The password string to be hashed
    Return: returns a salted hash of the pasword
    """
    p_bytes = password.encode('utf-8')
    p_salt = bcrypt.gensalt()
    p_hash = bcrypt.hashpw(p_bytes, p_salt)
    return p_hash


from db import DB
from user import User
from typing import TypeVar


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
