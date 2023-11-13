#!/usr/bin/python3
"""The BaseModel class."""

import uuid
from datetime import datetime
import  models


class BaseModel:
    """Defines all common attributes or methods for other classes."""

    def __init__(self, *args, **kwargs):
        """This method initializes a new BaseModel.

        Arguments:
            *args (any): This is unused.
            **kwargs (dict): This is key/value pairs of attributes.
        """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timeformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """This update updated_at varaible with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This returns the dictionary of the BaseModel instance. """
        odict = self.__dict__.copy()
        odict["created_at"] = self.created_at.isoformat()
        odict["updated_at"] = self.updated_at.isoformat()
        odict["__class__"] = self.__class__.__name__
        return odict

    def __str__(self):
        """This returns the str representation."""
        lname = self.__class__.__name__
        return "[{}] ({}) {}".format(lname, self.id, self.__dict__)
