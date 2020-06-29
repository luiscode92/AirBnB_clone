#!/usr/bin/python3
""" This module defines the class BaseModel"""

import sys
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    defines all common attributes/methods for BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        defines baseModel class
        """
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __set_attributes(self, attr_dict):
        """
        attr_dict to class attributes
        """

        del attr_dict['__class__']
        attr_dict['created_at'] = datetime.strptime(
                attr_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"
            )
        attr_dict['updated_at'] = datetime.strptime(
                attr_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"
            )
        for key, value in attr_dict.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Returns the String representation of a class
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the attribute updated_at with the current datetime
        """

        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of the instance:
        """
        dict_repre = self.__dict__.copy()
        dict_repre['__class__'] = self.__class__.__name__
        dict_repre["created_at"] = dict_repre['created_at'].isoformat()
        dict_repre['updated_at'] = dict_repre['updated_at'].isoformat()
        return dict_repre
