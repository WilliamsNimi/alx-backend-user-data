#!/usr/bin/env python3
""" Authentication module """
from flask import request
from typing import List, TypeVar


class Auth:
    """ This is the Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ ensures authentication is required
        @path: Argument for the route path
        @excluded_paths: Argument for paths that don't need authentication
        Return: Returns False """
        return False

    def authorization_header(self, request=None) -> str:
        """ adding authentication to the request header
        @request: a flask request object
        Return: Returns the authorization header with the request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user function
        @request: a flask request object
        Return: Returns the current user of the session"""
        return None
