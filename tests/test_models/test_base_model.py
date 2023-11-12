#!/usr/bin/python3

"""test BaseModel class"""
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
import json
import os
from datetime import datetime
import models



class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """ This backups the original file path and objects """
        self.orig_file_path = models.storage._FileStorage__file_path
        self.orig_objects = models.storage._FileStorage__objects

        """ This sets a temporary file path for testing """
        models.storage._FileStorage__file_path = "test_file.json"

        """ This creates a BaseModel instance for testing """
        self.ba_model = BaseModel()

    def tearDown(self):
        """ This restores the original file path and objects """
        models.storage._FileStorage__file_path = self.orig_file_path
        models.storage._FileStorage__objects = self.orig_objects

        """ This removes the temporary file if it exists """
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")

    def test_init(self):
        """ This tests the __init__ method """
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """ this tests the save method """
        init_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(init_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """ This tests the to_dict method """
        expted_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expted_dict)

    def test_str(self):
        """ This tests the __str__ method """
        expted_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expted_str)

    def test_save_reload(self):
        """ This tests the save and reload methods """
        init_updated_at = self.base_model.updated_at
        self.base_model.save()

        """ This creates a new BaseModel instance and reload from the file """
        nw_base_model = BaseModel(id=self.base_model.id)
        models.storage.reload()

        """ This checks if the reloaded instance has the correct updated_at """
        self.assertEqual(nw_base_model.updated_at, self.base_model.updated_at)

    def test_save_file_content(self):
        """ This test if the save method writes correct content to the file """
        self.base_model.save()
        with open("test_file.json", "r") as f:
            da = json.load(f)
        self.assertIn("BaseModel." + self.base_model.id, da)
