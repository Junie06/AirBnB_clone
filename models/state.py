#!/usr/bin/python3

"""
Defines the State model, which inherits from the BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state within the system.
    Inherits attributes and behaviors from the BaseModel.
    """

    # Attributes
    name: str = ""
