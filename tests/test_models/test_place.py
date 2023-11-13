#!/usr/bin/python3
"""Unittests for Place class."""
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):

    def setUp(self):
        """  Place for testing """
        self.place = Place()

    def tearDown(self):
        """ deletes after the test """
        del self.place

    def test_instance_creatn(self):
        """ This test the place object """
        self.assertIsInstance(self.place, Place)

    def test_attributes_initializatn(self):
        """ This test if the attributes of the
        place are initialized correctly
        """

        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertNotEqual(self.place.id, "")
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))


if __name__ == '__main__':
    unittest.main()
