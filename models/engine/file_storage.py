#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Manages storage of HBNB models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Query on the current database session all objects depending on the
        class name (argument cls)"""
        objs = {}
        if cls:
            for key, obj in self.__objects.items():
                if obj.__class__ == cls:
                    objs[key] = obj
        else:
            objs = self.__objects
        return objs

    def new(self, obj):
        """Add the object to the current database session"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize the objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(objs, f)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for key, val in objs.items():
                cls_name, obj_id = key.split('.')
                cls = models.classes[cls_name]
                self.__objects[key] = cls(**val)
        except:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects"""
        if obj in self.__objects.values():
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects.pop(key, None)
        elif obj is None:
            return

    def close(self):
        """Method that calls reload"""
        self.reload()
