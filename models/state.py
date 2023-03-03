#!/usr/bin/python3
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")
    
    @property
    def cities(self):
        """Returns the list of City instances with state_id equal to the current State.id"""
        from models import storage
        from models.city import City
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
