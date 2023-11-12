#!/usr/bin/python3
""" This defines test file_storage.py. """

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.engine.file_storage import FileStorage
import os
import json
from datetime import datetime


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_obj_empty(self):
        """ This tests all method when __objects is empty """
        res = self.file_storage.all()
        self.assertEqual(res, {})

    def test_all_with_obj_objects(self):
        """ this tests all method with objects in __objects """
        ob1 = BaseModel()
        ob2 = Amenity()
        self.file_storage.new(ob1)
        self.file_storage.new(ob2)
        res = self.file_storage.all()
        self.assertIn('BaseModel.' + obj.id, res)
        self.assertIn('Amenity.' + obj.id, res)

    def test_newmethod(self):
        """ This tests new method """
        ob = BaseModel()
        self.file_storage.new(ob)
        self.assertIn('BaseModel.' + ob.id, self.file_storage.all())

    def test_savemethod(self):
        """ This tests save method """
        ob = BaseModel()
        self.file_storage.new(ob)
        self.file_storage.save()

        """ This checks if the file was created """
        self.assertTrue(os.path.exists(self.file_path))

        """ This checks if the content is correct """
        with open(self.file_path, 'r') as file:
            da = json.load(file)
        self.assertIn('BaseModel.' + obj.id, da)

    def test_reloadmethod(self):
        """ This tests reload method """
        ob = BaseModel()
        self.file_storage.new(ob)
        self.file_storage.save()

        """ This modifies the file content """
        with open(self.file_path, 'w') as file:
            json.dump({"test": "data"}, file)

        """ This reloads and check if it reverts to the original content """
        self.file_storage.reload()
        res = self.file_storage.all()
        self.assertIn('BaseModel.' + obj.id, res)
        self.assertNotEqual(res, {"test": "data"})

    def test_reload_method_file_not_found(self):
        """ Test reload method when file not found """
        self.file_storage.reload()  

    def test_reload_method_empty_file(self):
        """ Test reload method with an empty file """
        with open(self.file_path, 'w') as file:
            file.write("")
        self.file_storage.reload()

    def test_reload_method_invalid_json(self):
        """ This tests reload method with invalid JSON """
        with open(self.file_path, 'w') as file:
            file.write("invalid json")
        self.file_storage.reload()

    def test_reload_method_exception(self):
        """ This tests reload method with a generic exception """
        with patch('builtins.open', side_effect=Exception):
            self.file_storage.reload()
