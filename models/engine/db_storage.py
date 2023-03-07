#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Manages storage of HBNB models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine and link to MySQL database"""
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
        db = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        Base.metadata.bind = self.__engine
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session
        all objects depending on class name"""
        objs = {}
        classes = [cls] if isinstance(cls, type) else \
            [BaseModel, User, State, City, Amenity, Place, Review]
        for c in classes:
            for obj in self.__session.query(c).all():
                key = obj.__class__.__name__ + '.' + obj.id
                objs[key] = obj
        return objs

    def new(self, obj):
        """Add the object to the current database session"""
        if isinstance(obj, BaseModel):
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create
        current database session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
        self.__session.configure(bind=self.__engine)
        return self.__session

    def close(self):
        """Method that closes the session"""
        if self.__session:
            self.__session.close()
