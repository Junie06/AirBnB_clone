#!/usr/bin/python3

"""
Defines the UserModel class, which inherits from the BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user within the system.
    Inherits attributes and behaviors from the BaseModel.
    """

    # Attributes
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
