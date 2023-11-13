#!/usr/bin/python3
"""City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Class city.

    Attributes:
        state_id (string): The state id.
        name (string): The name.
    """

    state_id = ""
    name = ""
