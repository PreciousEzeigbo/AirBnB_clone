#!/usr/bin/python3

"""Unit tests for city.py."""

import unittest
from models.city import City
from models.base_model import BaseModel
import models


class TestCity(unittest.TestCase):
    """Unit tests for the City class."""

    def test_city_inherits_from_base_model(self):
        """Test if City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attributes(self):
        """Test the attributes of the City class."""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_city_attribute_types(self):
        """Test the attribute types of the City class."""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_docstring(self):
        """Test the docstring of the City class."""
        self.assertIsNotNone(City.__doc__)
        self.assertIn(
            "state_id (str): The ID of the state to which the city belongs.",
            City.__doc__
            )
        self.assertIn("name (str): The name of the city.", City.__doc__)


if __name__ == "__main__":
    unittest.main()
