#!/usr/bin/python3
"""Test module for base_model module
Created by:
    Samuel Ezeh
    Emmanuel Ochoja
"""

from models import base_model
from models.base_model import BaseModel
import datetime
import inspect
import json
import unittest


class TestBaseModel(unittest.TestCase):
    """The test class for BaseModel
    """
    def setUp(self):
        """Creates a new instance before calling the test functions
        """
        self.base = BaseModel()
        self.functions = inspect.getmembers(BaseModel, inspect.isfunction)
    
    def test_module_docstring(self):
        """tests that module is documented
        """
        self.assertGreater(len(base_model.__doc__), 1)

    def test_class_documentation(self):
        """tests that class is documented
        """
        self.assertGreater(len(BaseModel.__doc__), 1)

    def test_function_documentation(self):
        """tests the documentation for functions
        """
        for name, function in self.functions:
            self.assertGreater(len(function.__doc__), 1)

    def test_type(self):
        """tests the instance types
        """
        self.assertTrue(isinstance(self.base, BaseModel))
        self.assertTrue(type(self.base), BaseModel)

    def test_id_is_unique(self):
        """tests that the id is unique
        """
        base_1 = BaseModel()
        self.assertFalse(base_1 == self.base)

    def test_id_is_string(self):
        """tests that id is string
        """
        self.assertTrue(type(self.base.id) is str)

    def test_created_at_is_datetime(self):
        """tests that the created_at is a datetime instance
        """
        created_at = self.base.created_at
        self.assertTrue(type(created_at) is datetime.datetime)
    
    def test_updated_at_is_datetime(self):
        """tests that the updated_at attribute is an instance of datetime
        """
        updated_at = self.base.updated_at
        self.assertTrue(type(updated_at) is datetime.datetime)

    def test_that_updated_at_diff_from_created_at(self):
        """tests that the created_at is different from updated_at
        """
        created_at = self.base.created_at
        updated_at = self.base.updated_at
        self.assertFalse(created_at == updated_at)

    def test_str(self):
        """tests that to string returns the string representation
        """
        string = "[{}] ({}) {}".format(self.base.__class__.__name__,
                                        self.base.id, self.base.__dict__)
        base_string = self.base.__str__()
        self.assertEqual(base_string, string)

    def test_that_str_returns_string(self):
        """tests that str() returns a string object
        """
        string = self.base.__str__()
        self.assertTrue(type(string) is str)

    def test_to_dict_returns_dict(self):
        """tests the to_dict instance methods
        """
        dictionary = self.base.to_dict()
        self.assertTrue(type(dictionary) is dict)

    def test_to_dict_keys_returned(self):
        """tests that the to_dict has the necessary attributes
        """
        dictionary = self.base.to_dict()
        self.assertTrue("id" in dictionary)
        self.assertTrue("created_at" in dictionary)
        self.assertTrue("updated_at" in dictionary)

    def testBaseModel_init_kwargs(self):
        """tests that the BaseModel can be initialised with keargs
        """
        dictionary = self.base.to_dict()
        new_obj = BaseModel(**dictionary)
        self.assertTrue(isinstance(new_obj, BaseModel))
        self.assertNotEqual(new_obj, self.base)

if __name__ == "__main__":
    unittest.main()
