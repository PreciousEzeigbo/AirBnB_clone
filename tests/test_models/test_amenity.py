#!/usr/bin/python3

"""Unit tests for amenity.py."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import models


class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class."""

    def test_amenity_inherits_from_base_model(self):
        """Test if Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_attributes(self):
        """Test the attributes of the Amenity class."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_amenity_attribute_type(self):
        """Test the attribute type of the Amenity class."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_docstring(self):
        """Test the docstring of the Amenity class."""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIn("name (str): The name of the amenity.", Amenity.__doc__)


if __name__ == "__main__":
    unittest.main()
