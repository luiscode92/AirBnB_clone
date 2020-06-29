#!/usr/bin/python3
"""
    Serialize and deserializes JSON file
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State

class FileStorage:
    """
    """
    __file_path = 'file.json'
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City
        }

    def all(self):
        """
         Returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj
        """

        name = obj.__class__.__name__

        self.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """
         Serialize __objects to the JSON file
        """
        with open(self.__file_path, "w") as f:
            obj_dict = {key: obj.to_dict()
                        for key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """
        asdad
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, val in obj_dict.items():
                    if val['__class__'] in FileStorage.__classes:
                        action = FileStorage.__classes
                        self.__objects[key] = action[val['__class__']](**val)
        except:
            pass
