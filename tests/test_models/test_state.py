#!/usr/bin/python3
"""Unittests for State class."""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_instance_creatn(self):
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_attribut(self):
        self.assertTrue(hasattr(self.state, 'name'))

    def test_attribute_type(self):
        self.assertIsInstance(self.state.name, str)

    def test_inherited_attribut(self):
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_created_at_ad_updated_at(self):
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_to_dict_meth(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(type(state_dict['created_at']), str)
        self.assertEqual(type(state_dict['updated_at']), str)

    def test_str_representatn(self):
        str_representation = str(self.state)
        self.assertTrue("[State]" in str_representation)
        self.assertTrue("id" in str_representation)
        self.assertTrue("created_at" in str_representation)
        self.assertTrue("updated_at" in str_representation)

if __name__ == '__main__':
    unittest.main()
