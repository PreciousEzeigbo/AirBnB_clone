#!/usr/bin/python3

"""A class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances."""

import json
import datetime
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """A class to manage data storage using JSON files."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves objects to the JSON file."""
        with open(FileStorage.__file_path, encoding='utf-8', mode='w') as file:
            new_dict = {
                k: v.to_dict()
                for k, v in FileStorage.__objects.items()
                }
            json.dump(new_dict, file)

    def reload(self):
        """Reloads objects from the JSON file."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    obj_class = eval(value["__class__"])
                    obj_instance = obj_class(**value)
                    self.__objects[key] = obj_instance
        except Exception:
            pass
