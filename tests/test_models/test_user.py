#!/usr/bin/python3

"""Unit tests for user.py."""

import unittest
from models.user import User
from models.base_model import BaseModel
import models


class TestUser(unittest.TestCase):
    """Unit tests for the User class."""

    def test_user_inherits_from_base_model(self):
        """Test if User inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_attributes(self):
        """Test the attributes of the User class."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_attribute_types(self):
        """Test the attribute types of the User class."""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_docstring(self):
        """Test the docstring of the User class."""
        self.assertIsNotNone(User.__doc__)
        self.assertIn(
            "email (str): The email address of the user.",
            User.__doc__
            )
        self.assertIn("password (str): The user's password.", User.__doc__)
        self.assertIn("first_name (str): The user's first name.", User.__doc__)
        self.assertIn("last_name (str): The user's last name.", User.__doc__)


if __name__ == "__main__":
    unittest.main()
