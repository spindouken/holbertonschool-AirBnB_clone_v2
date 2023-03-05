#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="user", cascade="all, delete")
    else:
        @property
        def places(self):
            """ Getter attribute in case of file storage """
            from models import storage
            from models.place import Place
            place_list = []
            for place in storage.all(Place).values():
                if place.user_id == self.id:
                    place_list.append(place)
            return place_list
