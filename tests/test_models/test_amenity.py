#!/usr/bin/python3
"""Unittests for Amenity class."""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """instance of Amenity  """
        self.amenity = Amenity()

    def tearDown(self):
        """ deletes after the test """
        del self.amenity

    def test_instance_creatn(self):
        """ Test  an instance of the Amenity class """
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes_initializatn(self):
        """ Test if the attributes of the amenity are initialized correctly """
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertNotEqual(self.amenity.id, "")
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

if __name__ == '__main__':
    unittest.main()
