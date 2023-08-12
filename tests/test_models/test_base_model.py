#!/usr/bin/python3

"""Unit tests for base_model.py."""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def test_init_with_kwargs(self):
        """Test initializing BaseModel instance with keyword arguments."""
        kwargs = {
            "id": "123",
            "created_at": "2023-01-01T12:00:00.000",
            "updated_at": "2023-01-01T12:30:00.000",
            "custom_attr": "value"
        }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.custom_attr, "value")
        self.assertEqual(obj.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 1, 1, 12, 30, 0))
        self.assertIsInstance(obj, BaseModel)

    def test_init_without_kwargs(self):
        """Test initializing BaseModel instance without keyword arguments."""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertIsInstance(obj, BaseModel)
        self.assertIs(
            models.storage.all().get(obj.__class__.__name__ + '.' + obj.id),
            obj
            )

    def test_save_method(self):
        """Test save method of BaseModel."""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_str_representation(self):
        """Test __str__ representation of BaseModel."""
        obj = BaseModel()
        str_rep = str(obj)
        self.assertIn("[BaseModel]", str_rep)
        self.assertIn(obj.id, str_rep)


if __name__ == "__main__":
    unittest.main()
