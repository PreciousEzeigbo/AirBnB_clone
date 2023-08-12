#!/usr/bin/python3

"""A class that inherits from BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """
    A class representing a city in a geographical state.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
