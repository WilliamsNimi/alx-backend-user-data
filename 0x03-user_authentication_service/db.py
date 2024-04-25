#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from typing import Mapping

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ This method adds a user to the db
        @email: email of the user
        @hashed_password: the hashed password fo the user
        Return: Returns the new user object
        """
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs):
        """ A method to search the db
        @query_str: the query to search for
        Return: Returns the first row where the query is found
        """
        users = self._session.query(User)
        if not users:
            raise NoResultFound
        if not kwargs:
            raise InvalidRequestError
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError
        found_user = self._session.query(User).filter_by(**kwargs).first()
        if not found_user:
            raise NoResultFound
        return found_user

    def update_user(self, user_id: int, **kwargs: Mapping) -> None:
        """ This method updates user based on id
        @user_id: user Id to be found
        Return: Returns none
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise ValueError
            else:
                setattr(user, key, value)
        self._session.commit()
        return None
