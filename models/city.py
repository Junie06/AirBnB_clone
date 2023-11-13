#!/usr/bin/python3

"""
Defines the City model, which inherits from the BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a City within the system.
    Inherits attributes and behaviors from the BaseModel.
    """

    # Attributes
    name: str = ""
    state_id: str = ""
