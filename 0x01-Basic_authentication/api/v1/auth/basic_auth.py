#!/usr/bin/env python3
""" the Basic Auth class """
from api.v1.auth.auth import Auth
import base64


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
