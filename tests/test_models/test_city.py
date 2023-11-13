#!/usr/bin/python3
"""Unittests for City class."""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):

    def setUp(self):
        """ instance of City"""
        self.city = City()

    def tearDown(self):
        """ deletes after the test """
        del self.city

    def test_instance_creatn(self):
        """ This test if the city object is an instance of the City class """
        self.assertIsInstance(self.city, City)

    def test_attributes_initializatn(self):
        """ This test if the attributes of the
        city are initialized correctly
        """

        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertNotEqual(self.city.id, "")
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))


if __name__ == '__main__':
    unittest.main()
