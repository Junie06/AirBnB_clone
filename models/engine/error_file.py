#!/usr/bin/python3

"""
Defines custom errors used in File Storage.
"""


class NotFoundModelError(Exception):

    """
    Raised when attempting to access an unregistered model.
    """
    def __init__(self, arg="BaseModel"):
        super().__init__(f"Model with name {arg} is not registered!")


class NotFoundInstanceError(Exception):

    """
    Raised when attempting to access an instance with an unknown ID.
    """
    def __init__(self, obj_id="", mod="BaseModel"):
        super().__init__(
                f"Instance of {mod} with id {obj_id} does not exist!")
