#!/usr/bin/python3
"""Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class.

    Classattributes:
        place_id (string): The Place.
        user_id (string): The User.
        text (string): The text.
    """

    place_id = ""
    user_id = ""
    text = ""
