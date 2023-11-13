#!/usr/bin/python3

"""
Defines the Amenity model, which inherits from the BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an Amenity in the system.
    Inherits attributes and behaviors from the BaseModel.
    """

    # Attributes
    name: str = ""
