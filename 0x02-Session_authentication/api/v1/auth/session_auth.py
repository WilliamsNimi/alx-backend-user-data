#!/usr/bin/env python3
""" session authentication module"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Sesstion Authentication class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ session creation method
        @user_id: user id with which to create a session
        Return: Returns a sessionID
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = uuid.uuid4()
        user_id_by_session_id[session_id] = user_id
        return session_id
