#!/usr/bin/python3
"""Unittests for Place class."""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_instance_creatn(self):
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_attribut(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_attribut_types(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_inherited_attribut(self):
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_created_at_ad_updated_at(self):
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_to_dict_meth(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)

    def test_str_representatn(self):
        str_representation = str(self.review)
        self.assertTrue("[Review]" in str_representation)
        self.assertTrue("id" in str_representation)
        self.assertTrue("created_at" in str_representation)
        self.assertTrue("updated_at" in str_representation)


if __name__ == '__main__':
    unittest.main()
