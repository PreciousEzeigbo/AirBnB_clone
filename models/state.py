#!/usr/bin/python3

"""A class that inherits from BaseModel."""

from models.base_model import BaseModel


class State(BaseModel):
    """
    A class representing a geographical state.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
