#!/usr/bin/python3

"""A class that inherits from BaseModel."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A class representing an amenity that can be associated with a place.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
