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
