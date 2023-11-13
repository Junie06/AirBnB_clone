#!/usr/bin/python3

"""
Defines the Review model, which inherits from the BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review within the system.
    Inherits attributes and behaviors from the BaseModel.
    """

    # Attributes
    place_id: str = ""
    user_id: str = ""
    text: str = ""
