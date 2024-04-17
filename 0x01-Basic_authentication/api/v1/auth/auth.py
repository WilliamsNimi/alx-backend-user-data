#!/usr/bin/env python3
""" Authentication module """
from flask import request
from Typing import List, TypeVar


class Auth:
    """ This is the Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ ensures authentication is required
        @path: Argument for the route path
        @excluded_paths: Argument for paths that don't need authentication
        Return: Returns False """
        return False

    def authorization_header(self, request=None) -> str:
        """ adding authentication to the request header"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns current user"""
        return request
