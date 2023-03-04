#!/usr/bin/python3
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
