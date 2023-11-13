#!/usr/bin/python3
"""FileStorage that serializes instances to a JSON file
     and deserializes JSON file to instances:.

"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.place import Place


class FileStorage:
    """This represents storage engine.

    Classattributes:
        __file_path (string): string - path to the JSON file.
        __objects (dictionary): dictionary - empty but will store all objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """This sets in __objects obj with key <obj_class_name>.id"""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """This serializes __objects to the JSON file path:__file_path."""
        data = FileStorage.__objects
        objdata = {obj: data[obj].to_dict() for obj in data.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdata, file)

    def reload(self):
        """This deserializes the JSON file to __objects  exists."""
        try:
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
                for o in data.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
