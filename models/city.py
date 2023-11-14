#!/usr/bin/python3
"""This is city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """The class city.

    Attributes:
        state_id (string): The state id.
        name (string): The name.
    """

    state_id = ""
    name = ""
