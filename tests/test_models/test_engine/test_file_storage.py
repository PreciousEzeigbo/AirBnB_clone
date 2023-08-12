#!/usr/bin/python3

"""Unit tests for file_storage.py."""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class in file_storage.py."""

    def setUp(self):
        """Set up test environment."""
        self.temp_file_path = "temp_test_file.json"
        FileStorage._FileStorage__file_path = self.temp_file_path
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

    def test_all_method(self):
        """Test the all method of FileStorage."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        """Test the new method of FileStorage."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save_and_reload_methods(self):
        """Test the save and reload methods of FileStorage."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = f"{type(obj).__name__}.{obj.id}"
        self.assertIn(key, new_storage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
