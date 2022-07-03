#!/usr/bin/python
"""
file storage module
"""
from datetime import datetime
from typing import Type
from models.base_model import BaseModel
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ A class called FileStorage
    attributes:
    attr1(__file_path): JSON file path
    attr2(__objects): dictionary"""
    __file_path = "file.json"
    open(__file_path, "a")
    __objects = {}

    def all(self):
        """ return dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """ save to JSON"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """reload from JSON"""

        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj = json.load(f)
            for k, v in obj.items():
                class_name = k.split('.')[0]
                self.__objects[k] = eval(class_name)(**v)
        except TypeError:
            pass
