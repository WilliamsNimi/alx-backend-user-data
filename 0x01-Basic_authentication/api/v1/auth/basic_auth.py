#!/usr/bin/env python3
""" the Basic Auth class """
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ The basic Auth class extends Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ gettin base64 header
        @authorization_header: the authorization header to be authenticated
        Return: Returns base64 of the header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.startswith('Basic '):
            return authorization_header[6:]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decoding base64 encoding
        @base64_authorization_header: encoded text in base64
        Return: returns the decoded value of a string as utf 8
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            encoding = base64.b64decode(base64_authorization_header)
            return encoding.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extracting user credentials
        @decode_base64_authorization_header: decoded header
        Return: Returns 2 values
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        split_text = decoded_base64_authorization_header.split(':', 1)
        return split_text[0], split_text[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ validating user method
        @user_email: the email of the user
        @user_pwd: the password of the user
        Return: returns the user instance
        """
        if user_email is None or type(user_email) is not a str:
            return None
        if user_pwd is None or type(user_pwd) is not a str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
