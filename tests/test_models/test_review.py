#!/usr/bin/python3

"""Unit tests for review.py."""

import unittest
from models.review import Review
from models.base_model import BaseModel
import models


class TestReview(unittest.TestCase):
    """Unit tests for the Review class."""

    def test_review_inherits_from_base_model(self):
        """Test if Review inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_attributes(self):
        """Test the attributes of the Review class."""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review_attribute_types(self):
        """Test the attribute types of the Review class."""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)


if __name__ == "__main__":
    unittest.main()
