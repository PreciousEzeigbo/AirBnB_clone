#!/usr/bin/python3

"""A class that inherits from BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class representing a review for a place or accommodation.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
