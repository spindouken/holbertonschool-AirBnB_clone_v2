#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """ Review Getter attribute in case of file storage """
            from models import storage
            from models.review import Review
            review_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Getter attribute in case of file storage"""
            from models import storage
            from models.amenity import Amenity
            amenity = []
            dicty = storage.all(Amenity)

            for amenity_inst in dicty.values():
                if amenity_inst.id == self.amenity_id:
                    amenity.append(amenity_inst)
            return amenity

        @amenities.setter
        def amenities(self, amenity_list):
            """Set attribute in case of file storage"""
            from models.amenity import Amenity
            for amen in amenity_list:
                if type(amen) == Amenity:
                    self.amenity_ids.append(amen)
