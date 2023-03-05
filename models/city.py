#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        @property
        def places(self):
            """ Getter attribute in case of file storage """
            from models import storage
            from models.place import Place
            place_list = []
            for place in storage.all(Place).values():
                if place.city_id == self.id:
                    place_list.append(place)
            return place_list
