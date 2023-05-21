#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel


Class TestState(unittest.TestCase):
    """A class to test State class"""
    def setUp(self):
        self.state = State()
        self.state.name = "Abia"

    def tearDown(self):
        del self.state

    def test_state_has_attr(self):
        """Check for the presence of attributes in State class"""
        self.assertTrue('name' in self.state.__dict__)
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)

    def test_attr_type(self):
        """Test for attributes type"""
        self.assertTrue(type(self.state.name) is str)
        self.assertTrue(type(self.state.id) is str)
        self.assertTrue(type(self.state.created_at) is str)
        self.assertTrue(type(self.state.updated_at) is str)

if __name__ == "__main__":
    unittest.main()
