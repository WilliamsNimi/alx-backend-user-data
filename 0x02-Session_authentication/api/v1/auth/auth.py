#!/usr/bin/env python3
""" Authentication module """
import re
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ This is the Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ ensures authentication is required
        @path: Argument for the route path
        @excluded_paths: Argument for paths that don't need authentication
        Return: Returns True or False based on exitence of Path """
        if path is None or excluded_paths is None:
            return True
        if excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        for route in excluded_paths:
            if re.match(route.replace('*', '.*'), path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ adding authentication to the request header
        @request: a flask request object
        Return: Returns the authorization header with the request object"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user function
        @request: a flask request object
        Return: Returns the current user of the session"""
        return None

    def session_cookie(self, request=None):
        """ getting session cookie
        @request: Request to be examined
        Return: Return the session cookie
        """
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
