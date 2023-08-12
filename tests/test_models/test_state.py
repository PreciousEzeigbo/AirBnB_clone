#!/usr/bin/python3

"""Unit tests for state.py."""

import unittest
from models.state import State
from models.base_model import BaseModel
import models


class TestState(unittest.TestCase):
    """Unit tests for the State class."""

    def test_state_inherits_from_base_model(self):
        """Test if State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_attributes(self):
        """Test the attributes of the State class."""
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_state_attribute_type(self):
        """Test the attribute type of the State class."""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_docstring(self):
        """Test the docstring of the State class."""
        self.assertIsNotNone(State.__doc__)
        self.assertIn("name (str): The name of the state.", State.__doc__)


if __name__ == "__main__":
    unittest.main()
