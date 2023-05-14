#!/usr/bin/python3
"""Test for User class module
Created by:
    Emmanuel Ochoja
    Samuel Ezeh
"""

import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test user class"""
    def setUp(self):
        self.user = User()
        self.user.firstname = "Emmanuel"
        self.user.lastname = "Ochoja"
        self.user.email = "emmanuelochoja@mail.com"
        self.user.password = "password"

    def tearDown(self):
        del self.user

    def test_user_attr_type(self):
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.lasst_name), str)
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)

        self.assertEqual(type(self.user.id), str)
        self.assertEqual(type(self.user.created_at), str)
        self.assertEqual(type(self.user.updated_at), str)

    def test_user_has_attr(self):
        """Verify that attributes are present in user instance"""
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)

    def test_save(self):
        """Verify that changes made were saved"""
        self.assertFalse(self.user.updated_at == self.user.created_at)


if __name__ == "__main__":
    unittest.main()
