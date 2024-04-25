#!/usr/bin/env python3
""" Password authentication module """
import bcrypt
from db import DB
from user import User
from typing import TypeVar, Union
import uuid


def _hash_password(password: str) -> bytes:
    """ Password hash method
    @password: The password string to be hashed
    Return: returns a salted hash of the pasword
    """
    p_bytes = password.encode('utf-8')
    p_salt = bcrypt.gensalt()
    p_hash = bcrypt.hashpw(p_bytes, p_salt)
    return p_hash


def _generate_uuid() -> str:
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

    def get_user_from_session_id(self, session_id: str) -> Union[None, User]:
        """ function to get user associated with a session id
        @session_id: session id to search for
        Return: Returns the User found or none if not found
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ User session destruction function
        @user_id: User id to find user whose session is to be destroyed
        Return: None
        """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """ password reset function"""
        try:
            user = self._db.find_user_by(email=email)
            user_uuid = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return user_uuid
        except Exception:
            raise ValueError()

    def update_password(self, reset_token: str, password: str) -> None:
        """ update user password function
        @reset_token: This token tracks update
        @password: new password
        Return: Returns None
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            self._db.update_user(user.id,
                                 hashed_password=_hash_password(password),
                                 reset_token=None)
            return None
        except Exception:
            raise ValueError
        return None
